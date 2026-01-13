# tasks/task1_get_folders.py
from api.client import APIClient
from config.settings import BASE_URL
from utils.validator import validate_response_structure, validate_api_success

def execute_task1(api_token=None):
    """Task #1: GET all drive folders"""
    print("\n" + "#"*100)
    print("# TASK #1: GET All Drive Folders")
    print("#"*100)
    
    client = APIClient(BASE_URL, api_token)
    response_data = client._make_request("GET", "", expected_status=200)
    
    if not response_data:
        return None
    
    # Validate response structure
    required_keys = ["success", "data"]
    if not validate_response_structure(response_data, required_keys):
        return None
    
    # Check if success is true
    if not validate_api_success(response_data):
        return None
    
    # Extract data
    data = response_data.get("data", [])
    if isinstance(data, list):
        print(f" Retrieved {len(data)} folders")
        for folder in data:
            if isinstance(folder, dict) and "id" in folder and "title" in folder:
                print(f"   - Folder: {folder.get('title')} (ID: {folder.get('id')})")
                # Show subfolders if any
                sub_folders = folder.get("sub_folders", [])
                for sub in sub_folders:
                    if isinstance(sub, dict):
                        print(f"      └─ {sub.get('title')} (ID: {sub.get('id')})")
    
    return response_data