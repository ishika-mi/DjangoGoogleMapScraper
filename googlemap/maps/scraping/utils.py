import json
import os
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(filename='maps/info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument("--disable-popup-blocking")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrap_element(element, by, locator):
    """
    Locates and returns an element based on the provided locating strategy and expression.

    Args:
        element: The parent element within which to locate the element.
        by: The locating strategy to be used.
        locator: The locator expression to find the element.

    Returns:
        obj: The located element or None if not found.
    """
    try:
        element = WebDriverWait(element, 5).until(EC.presence_of_all_elements_located((by, locator)))
        if len(element) == 1:
            return element[0]
        elif not element:
            return ''
        else:
            return element
    except Exception as e:
        logging.info(f"Error while finding the element {e}")
    
    
def scrap_element_attribute_for_link(element, by, locator, attribute):
    """
    Scrapes a specific attribute from a list of elements and returns a list of attribute values.

    Args:
        element: The parent element within which to locate elements.
        by: The locating strategy to be used.
        locator: The locator expression to find elements.
        attribute: The attribute name to be scraped from elements.

    Returns:
        list: A list of attribute values scraped from the elements.
    """
    try:
        element = WebDriverWait(element, 5).until(EC.presence_of_all_elements_located((by, locator)))
        elements_list = [ele.get_attribute(attribute) for ele in element]
        return elements_list or None
    except Exception as e:
        logging.info(f"Error while finding the element {e}")
    

def scrap_element_attribute(element, by, locator, attribute):
    """
    Scrapes a specific attribute from an element and returns its value.

    Args:
        element: The parent element within which to locate the element.
        by: The locating strategy to be used.
        locator: The locator expression to find the element.
        attribute: The attribute name to be scraped from the element.

    Returns:
        str: The attribute value scraped from the element.
    """
    try:
        element = WebDriverWait(element, 5).until(EC.presence_of_all_elements_located((by, locator)))
        if type(element) == list:
            element = element[0]
        return element.get_attribute(attribute) if element else None
    except Exception as e:
        logging.info(f"Error while finding the element {e}")
    

def click_button_exception(element, browser):
    """
    Clicks a button element using JavaScript and handles exceptions.

    Args:
        element: The element to be clicked.
        browser: The browser instance.

    Returns:
        None
    """
    if element:
        try:
            element = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(element))
            browser.execute_script("arguments[0].click();", element)
        except Exception as e:
            logging.info(f"Error while finding the element {e}")

def add_data_to_json(element,filename):
    with open(f'jsonfiles/{filename}.json', 'w') as json_file:
        json.dump(element, json_file, indent=4)
    return element

def scroll(browser,element):
    """
    Scrolls the web page to the middle position.

    Args:
        browser: The browser instance.

    Returns:
        None
    """
    SCROLL_PAUSE_TIME = 2.5
    scroll_no = 1
    last_height = browser.execute_script("return arguments[0].scrollHeight;", element)

    while True:
        browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", element)
        logging.info(f"Scrolled for {scroll_no} time")
        scroll_no+=1
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return arguments[0].scrollHeight;", element)
        if new_height == last_height:
            logging.info("Scrolling Complete - Reached to the end of the webpage")
            break
        last_height = new_height

def add_data_to_json(element,filename):
    if not os.path.exists('jsonfiles'):
        os.makedirs('jsonfiles')
    with open(f'jsonfiles/{filename}.json', 'a') as json_file:
        json.dump(element, json_file, indent=4)
    return element