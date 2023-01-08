import mysql.connector
from dotenv import load_dotenv
import os

class SQL:
    def __init__(self):
        self.cursor, self.mydb = self.DatabaseAuth()

    def DatabaseAuth(self):

        # # # # Database Credentials # # # # #
        load_dotenv()
        HOSTNAME = os.getenv('DB_HOSTNAME')
        USER = os.getenv('DB_USERNAME')
        PASSWORD = os.getenv('DB_PASSWORD')
        DATABASE = os.getenv('DB_DATABASE')

        # # # # Connect to MySQL # # # #

        mydb = mysql.connector.connect(
            host = HOSTNAME,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )
        # Create cursor
        cursor = mydb.cursor(buffered=True)

        return cursor, mydb



