import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r"C:\Users\emart\Desktop\sol para todos\sol-para-todos\sol-para-todos\.env")

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )