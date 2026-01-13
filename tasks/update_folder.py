# tasks/task3_update_folder.py
from api.folder_client import FolderAPIClient
from config.settings import BASE_URL

def execute_task3(folder_id, new_title, api_token=None):
    """Execute Task #3: PUT update folder name"""
    client = FolderAPIClient(BASE_URL)
    
    if api_token:
        client.set_api_token(api_token)
    
    return client.update_folder_name(folder_id, new_title)