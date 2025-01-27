import psycopg2
import os
from dotenv import load_dotenv


def connect_to_db():
    load_dotenv()    
    conn = psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        user=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        port=os.getenv("PORT") 
    )
    return conn