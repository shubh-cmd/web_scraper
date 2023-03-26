import csv
from datetime import date as dt
import sqlite3

class Utils:
    @staticmethod
    def create_csv_file(file_data):

        # Generate a csv file to store the news data
        today = dt.today().strftime('%d%m%Y')
        filename = f'{today}_verge.csv'
        fields = ['id', 'URL', 'headline', 'author', 'date']

        with open(filename, 'w') as file:

            writer = csv.writer(file)

            writer.writerow(fields)
            writer.writerows(file_data) 

    @staticmethod
    def create_database(file_data):
        # Create SQLite database connection
        connection = sqlite3.connect('sqlite3.db')
        cursor = connection.cursor()

        # Create the articles Table in the database
        cursor.execute('''CREATE TABLE IF NOT EXISTS articles
        (id INTEGER PRIMARY KEY, url TEXT, headline TEXT, author TEXT, date TEXT)''')

        # Insert data into the database ony by one
        for obj in file_data:

            id,url,headline,author,date = obj
            # Check if article already exists in database
            cursor.execute("SELECT id FROM articles WHERE url=?", (url,))
            tuple = cursor.fetchone()

            if tuple is None:

                cursor.execute("INSERT INTO articles (id, url, headline, author, date) VALUES (?, ?, ?, ?, ?)",
                            (id, url, headline, author, date))
                connection.commit()

        connection.close()