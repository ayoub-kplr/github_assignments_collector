import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

TARGET = os.getenv('TARGET')

ORG = os.getenv('ORG')

CSV_DIR = os.getenv("CSV_DIR")