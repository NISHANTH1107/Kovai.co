# tasks/task2_create_folder.py
from api.client import APIClient
from config.settings import BASE_URL, GlobalState, USER_ID
from utils.validator import validate_response_structure, validate_api_success

def execute_task2(folder_title, parent_folder_id=None, api_token=None):
    """Task #2: POST create a new folder"""
    print("\n" + "#"*100)
    print("# TASK #2: POST Create a New Folder")
    print("#"*100)
    
    client = APIClient(BASE_URL, api_token)
    
    # Prepare request body
    body = {
        "title": folder_title,
        "user_id": USER_ID
    }
    
    if parent_folder_id and parent_folder_id.strip():
        body["parent_folder_id"] = parent_folder_id
    
    response_data = client._make_request("POST", "", data=body, expected_status=[200, 201])
    if not response_data:
        return None
    
    # Validate response structure
    required_keys = ["success"]
    if not validate_response_structure(response_data, required_keys):
        return None
    
    # Check if success is true
    if not validate_api_success(response_data):
        return None
    
    # Extract folder data
    folder_data = response_data.get("data", {})
    if isinstance(folder_data, dict) and "id" in folder_data and "title" in folder_data:
        folder_id = folder_data.get("id")
        folder_title = folder_data.get("title")
        print(f" Folder Created Successfully!")
        print(f"   - Title: {folder_title}")
        print(f"   - ID: {folder_id}")
        
        # Store folder ID globally
        GlobalState.set_created_folder_id(folder_id)
        
        return response_data
    else:
        print(" ERROR: Response data does not contain expected folder information")
        return None