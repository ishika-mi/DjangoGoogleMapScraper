import psycopg2
import logging

logging.basicConfig(filename='maps/info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432,
            database="mapscraper"
        )
        logging.info("Connected to PostgreSQL database successfully!")
        return connection
    except (Exception, psycopg2.Error) as error:
        logging.error("Error while connecting to PostgreSQL", error)
        return None


def insert_data(search_text, item):
    connection = create_connection()
    try:
        add_data_in_database(connection, item, search_text)
    except (Exception, psycopg2.Error) as error:
        logging.error("Error while inserting data into PostgreSQL", error)
        connection.rollback()
    finally:
        connection.close()

def add_data_in_database(connection, item, search_text):
    cursor = connection.cursor()
    if not item['business_title']:
        return None
    unique_key_fields = ["business_title", "address"]
    unique_key_conditions = ' AND '.join(f'{name} = %s' for name in unique_key_fields)
    select_query = f"""SELECT id FROM maps_locationdetails WHERE {unique_key_conditions}"""
    cursor.execute(select_query,(item['business_title'], item['address']))
    if id_value := cursor.fetchone():
        update_query = f''' UPDATE maps_locationdetails SET business_title = %s, address = %s, website = %s, phone_number = %s WHERE id = {id_value[0]}'''
        cursor.execute(update_query, (item['business_title'], item['address'], item['website'], item['phone_number']))
    else:
        insert_query = '''INSERT INTO maps_locationdetails (search_text, business_title, address, website, phone_number) VALUES (%s, %s, %s, %s, %s) '''
        cursor.execute(insert_query, (search_text, item['business_title'], item['address'], item['website'], item['phone_number']))
    connection.commit()
    logging.info("Data inserted successfully!")
