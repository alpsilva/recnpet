from firebase_admin import credentials
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:\\Dev\\hacka\\recnpet\\backend\\database\\.env")

db_url = os.getenv("DB_URL")

certificate_file_path = "./database/serviceAccountKey.json"
database_credentials = credentials.Certificate(certificate_file_path)
database_config = {
    'databaseURL': db_url
}