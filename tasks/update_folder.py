# tasks/task3_update_folder.py
from api.client import APIClient
from config.settings import BASE_URL
from utils.validator import validate_response_structure, validate_api_success

def execute_task3(folder_id, new_title, api_token=None):
    """Task #3: PUT update folder name"""
    print("\n" + "#"*100)
    print("# TASK #3: PUT Update Folder Name")
    print("#"*100)
    
    if not folder_id:
        print(" ERROR: Invalid folder ID provided")
        return None
    
    client = APIClient(BASE_URL, api_token)
    
    # Prepare request body
    body = {
        "title": new_title
    }
    
    response_data = client._make_request("PUT", f"/{folder_id}", data=body, expected_status=200)
    if not response_data:
        return None
    
    # Validate response structure
    required_keys = ["success"]
    if not validate_response_structure(response_data, required_keys):
        return None
    
    # Check if success is true
    if not validate_api_success(response_data):
        return None
    
    # Extract updated folder data
    folder_data = response_data.get("data", {})
    if isinstance(folder_data, dict) and "title" in folder_data:
        updated_title = folder_data.get("title")
        print(f" Folder Updated Successfully!")
        print(f"   - New Title: {updated_title}")
        return response_data
    else:
        print(" ERROR: Response data does not contain expected folder information")
        return None