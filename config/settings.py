# config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = "https://apihub.document360.io/v2/Drive/Folders"

# Headers template
HEADERS = {
    "api_token": os.getenv("API_TOKEN", ""),
    "Content-Type": "application/json"
}

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