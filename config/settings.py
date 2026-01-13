# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
USER_ID = os.getenv("USER_ID")
print(USER_ID)

# Global state
class GlobalState:
    created_folder_id = None
    
    @classmethod
    def set_created_folder_id(cls, folder_id):
        cls.created_folder_id = folder_id
    
    @classmethod
    def get_created_folder_id(cls):
        return cls.created_folder_id
    
    @classmethod
    def clear_created_folder_id(cls):
        cls.created_folder_id = None

def get_headers(api_token=None):
    """Get headers with optional API token override"""
    token = api_token or API_TOKEN
    headers = {
        "Content-Type": "application/json",
        "user_id": USER_ID
    }
    if token:
        headers["api_token"] = token
    return headers