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

- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. 
- It’s free and open source. It follows the model-view-template (MVT) architectural pattern. Django aims to make it easier to build web applications by providing reusable components and a robust development environment.

#### Features

- Batteries-Included: Django comes with a variety of built-in features for web development, such as an ORM (Object-Relational Mapper), authentication system, URL routing, template engine, and more.

- Admin Interface: Django provides a powerful admin interface out-of-the-box, which allows developers to manage application data through a web-based interface without writing custom code.

- Security: Django helps developers avoid many common security mistakes by providing built-in protection against XSS, CSRF, SQL injection, and clickjacking.

- Scalability: Django applications can scale well both vertically and horizontally. With proper architecture and optimization, Django can handle heavy traffic loads.

- Versatility: Django is suitable for building different types of web applications, including content management systems (CMS), social networks, e-commerce platforms, and more.

- Community and Ecosystem: Django has a large and active community of developers, which means plenty of resources, packages, and third-party integrations are available.

#### Getting Started with Django
- **Installation:** You can install Django using pip, Python's package manager:
    ```bash
    pip install django
- **Creating a Django Project:** Once Django is installed, you can create a new Django project using the following command:
    ```bash
    django-admin startproject <myproject>
- **Running the Development Server:** You can start the Django development server using the following command. This will start the development server on http://127.0.0.1:8000/ by default:
    ```bash
    cd <myproject>
    python manage.py runserver
- **Creating Apps:** Django projects are composed of one or more apps. You can create a new app within your project using the following command:
    ```bash
    python manage.py startapp myapp
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
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

## Steps for Database Setup
1. Before running any postgresql commands we need to switch user to postgres:
    ```bash
    sudo -u postgres psql
2. Create Database
    ```bash
   CREATE DATABASE <DATABASE_NAME>;
3. Create User
   ```bash
   CREATE USER <USERNAME> WITH PASSWORD '<PASSWORD>';
4. Grant Database privileges to User
    ```bash  
    GRANT ALL PRIVILEGES ON DATABASE <DATABASE_NAME> to <USERNAME>;
5. Exit
    ```bash
    \q
