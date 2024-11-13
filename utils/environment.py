import os
from dotenv import load_dotenv

# Environment
load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
USER_USERNAME = os.getenv("LOGIN_USERNAME")
