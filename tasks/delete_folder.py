# tasks/task4_delete_folder.py
from api.client import APIClient
from config.settings import BASE_URL
from utils.validator import validate_api_success

def execute_task4(folder_id, api_token=None):
    """Task #4: DELETE the folder"""
    print("\n" + "#"*100)
    print("# TASK #4: DELETE the Folder")
    print("#"*100)
    
    if not folder_id:
        print(" ERROR: Invalid folder ID provided")
        return False
    
    client = APIClient(BASE_URL, api_token)
    response_data = client._make_request("DELETE", f"/{folder_id}", expected_status=[200, 204])
    
    # If no response data (empty response for 204), consider it success
    if response_data is None:
        print(f" Folder Deleted Successfully! (204 No Content)")
        print(f"   - Folder ID: {folder_id}")
        return True
    
    # If we have response data, check for success field
    if isinstance(response_data, dict):
        if "success" in response_data:
            if not validate_api_success(response_data):
                return False
            else:
                print(f" Folder Deleted Successfully!")
                print(f"   - Folder ID: {folder_id}")
                return True
    
    # If we get here without returning, something unexpected happened
    print(f" Unexpected response format for deletion")
    return False