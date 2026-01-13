# tasks/task2_create_folder.py
from api.folder_client import FolderAPIClient
from config.settings import BASE_URL

def execute_task2(folder_title, parent_folder_id=None, api_token=None):
    """Execute Task #2: POST create a new folder"""
    client = FolderAPIClient(BASE_URL)
    
    if api_token:
        client.set_api_token(api_token)
    
    return client.create_folder(folder_title, parent_folder_id)