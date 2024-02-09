# GoogleMapScraping
*Google Maps scraping allows user to get business locations' details of the location within few clicks!*

Google Maps scraper can provide businesses with valuable location-based data that can be used for market analysis, local SEO optimization, lead generation, targeted advertising, logistics optimization, and business expansion efforts. 

## Steps to follow:
### Give location name as input file in home page and click scrap button
![Home Page](<googlemap/maps/static/Screenshot from 2024-02-09 13-11-38.png>)
-  Website will start scraping business locations' details for the given input 
- Website will be loading till scraping process gets completed. (NOTE: scraping speed depends on number of locations available for given input)

### Download CSV button will be available once the scraping process gets completed.
![CSV Download Page](<googlemap/maps/static/Screenshot from 2024-02-09 13-19-03.png>)
- Click on download csv button to download csv of your desired place

And That's it!!!!! You will be having location details for your desired place in csv file

## Libraries Used

### Django
*For developing website(both frontend and backend)*

Django is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views architectural pattern.

### Selenium
*For Scraping Process*

Web Scraping with Selenium allows you to gather all the required data using Selenium Webdriver Browser Automation. Selenium crawls the target URL webpage and gathers data at scale. 

## Steps for Project Setup
1. Clone the repository:
    ```bash
    git clone <REPOSITORY URL>
    cd GoogleMapScraping
2. Install the required libraries by running the following command:

   ```bash
   pip install -r requirements.txt
3. Run website
    ```bash  
    cd googlemap
    python3 manage.py runserver
