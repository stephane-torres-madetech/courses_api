import psycopg2
import os
from dotenv import load_dotenv

class Database():
    def __init__(self):
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        load_dotenv()    
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT") 
        )
        return conn
    
    def close_connection(self):
        self.connection.close()