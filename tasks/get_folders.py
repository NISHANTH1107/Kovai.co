# tasks/task1_get_folders.py
from api.folder_client import FolderAPIClient
from config.settings import BASE_URL

def execute_task1(api_token=None):
    """Execute Task #1: GET all drive folders"""
    client = FolderAPIClient(BASE_URL)
    
    if api_token:
        client.set_api_token(api_token)
    
    return client.get_all_folders()