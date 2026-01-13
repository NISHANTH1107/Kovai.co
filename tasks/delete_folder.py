# tasks/task4_delete_folder.py
from api.folder_client import FolderAPIClient
from config.settings import BASE_URL

def execute_task4(folder_id, api_token=None):
    """Execute Task #4: DELETE the folder"""
    client = FolderAPIClient(BASE_URL)
    
    if api_token:
        client.set_api_token(api_token)
    
    return client.delete_folder(folder_id)