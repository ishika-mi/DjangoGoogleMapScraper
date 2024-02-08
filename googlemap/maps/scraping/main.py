import time

from .pipelines import insert_data
from .utils import chrome_options, scrap_element, click_button_exception, scrap_element_attribute, scrap_element_attribute_for_link, scroll
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(filename='maps/info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def start_scraper(search_text):
    browser = chrome_options()
    browser.get('https://www.google.com/maps/search/')
    try:
        send_location = scrap_element(browser, By.CSS_SELECTOR, "input.searchboxinput")
        send_location.send_keys(search_text)
        search_click_button = scrap_element(browser, By.CSS_SELECTOR, "button#searchbox-searchbutton")
        click_button_exception(search_click_button, browser)
        logging.info(f"Searched for {search_text}")
        time.sleep(0.5)
        scroll_element = scrap_element(browser, By.XPATH, "//div[contains(@aria-label,'Results for')]")
        scroll(browser, scroll_element)
        parse(browser, search_text)
        send_location.clear()
    finally:
        browser.quit()

def parse(browser, search_text):
    location_links = scrap_element_attribute_for_link(browser, By.XPATH,
                                                      "//div[contains(@class,'TFQHme')]/preceding-sibling::div[1]/div/a",
                                                      attribute='href')
    logging.info("Scraped Location links Successfully!!!")
    for link in location_links:
        browser.execute_script(f'window.open("{link}");')
        browser.switch_to.window(browser.window_handles[1])
        scrap_location_details(browser,search_text)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        
def scrap_location_details(browser,search_text):
    browser_data = scrap_element(browser,By.CLASS_NAME,'w6VYqd')
    business_title = scrap_element_attribute(browser_data, By.TAG_NAME, 'h1', attribute='innerText')
    address = scrap_element_attribute(browser_data, By.XPATH, "//button[contains(@data-item-id,'address')]",
                                      attribute='aria-label')
    address = address.replace('Address: ', '') if address else None
    open_hours = scrap_element_attribute(browser_data, By.XPATH,
                                          "//div[contains(@aria-label,'Hide open hours for the week')]",
                                          attribute='aria-label')
    open_hours = open_hours.replace(" Hide open hours for the week", "").replace("\u202f", '') if open_hours else None
    company_website = scrap_element_attribute(browser_data, By.XPATH, "//a[contains(@aria-label,'Website')]",
                                              attribute='href')
    phone_number = scrap_element_attribute(browser_data, By.XPATH, "//button[contains(@aria-label,'Phone')]",
                                           attribute='data-item-id')
    phone_number = phone_number.replace("phone:tel:", "") if phone_number else None
    logging.info(f"Scraped data for {business_title}")
    
    location_data =  {
        'business_title': business_title,
        'address': address,
        'website': company_website,
        'phone_number': phone_number,
    }
    logging.info(f"Details are as Follows:\n {location_data}")
    insert_data(search_text, location_data)