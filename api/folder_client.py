# api/folder_client.py
from api.base_client import BaseAPIClient
from utils.validator import validate_response_structure, validate_api_success
from config.settings import GlobalState

class FolderAPIClient(BaseAPIClient):
    def __init__(self, base_url):
        super().__init__(base_url)
    
    def get_all_folders(self):
        """Task #1: GET all drive folders"""
        print("\n" + "#"*80)
        print("# TASK #1: GET All Drive Folders")
        print("#"*80)
        
        response_data = self._make_request("GET", "", expected_status=200)
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
            print(f"✅ Retrieved {len(data)} folders")
            for folder in data:
                if isinstance(folder, dict) and "id" in folder and "title" in folder:
                    print(f"   - Folder: {folder.get('title')} (ID: {folder.get('id')})")
                    # Show subfolders if any
                    sub_folders = folder.get("sub_folders", [])
                    for sub in sub_folders:
                        if isinstance(sub, dict):
                            print(f"      └─ {sub.get('title')} (ID: {sub.get('id')})")
        
        return response_data
    
    def create_folder(self, folder_title, parent_folder_id=None):
        """Task #2: POST create a new folder"""
        print("\n" + "#"*80)
        print("# TASK #2: POST Create a New Folder")
        print("#"*80)
        
        # Prepare request body - API uses "title" not "name"
        body = {
            "title": folder_title
        }
        
        if parent_folder_id and parent_folder_id.strip():
            body["parent_folder_id"] = parent_folder_id
        
        response_data = self._make_request("POST", "", data=body, expected_status=[200, 201])
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
            print(f"✅ Folder Created Successfully!")
            print(f"   - Title: {folder_title}")
            print(f"   - ID: {folder_id}")
            
            # Store folder ID globally
            GlobalState.set_created_folder_id(folder_id)
            
            return response_data
        else:
            print("❌ ERROR: Response data does not contain expected folder information")
            return None
    
    def update_folder_name(self, folder_id, new_title):
        """Task #3: PUT update folder name"""
        print("\n" + "#"*80)
        print("# TASK #3: PUT Update Folder Name")
        print("#"*80)
        
        if not folder_id:
            print("❌ ERROR: Invalid folder ID provided")
            return None
        
        # Prepare request body - API uses "title" not "name"
        body = {
            "title": new_title
        }
        
        response_data = self._make_request("PUT", f"/{folder_id}", data=body, expected_status=200)
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
            print(f"✅ Folder Updated Successfully!")
            print(f"   - New Title: {updated_title}")
            return response_data
        else:
            print("❌ ERROR: Response data does not contain expected folder information")
            return None
    
    def delete_folder(self, folder_id):
        """Task #4: DELETE the folder"""
        print("\n" + "#"*80)
        print("# TASK #4: DELETE the Folder")
        print("#"*80)
        
        if not folder_id:
            print("❌ ERROR: Invalid folder ID provided")
            return False
        
        response_data = self._make_request("DELETE", f"/{folder_id}", expected_status=[200, 204])
        
        # If no response data (empty response for 204), consider it success
        if response_data is None:
            print(f"✅ Folder Deleted Successfully! (204 No Content)")
            print(f"   - Folder ID: {folder_id}")
            return True
        
        # If we have response data, check for success field
        if isinstance(response_data, dict):
            if "success" in response_data:
                if not response_data.get("success"):
                    print("❌ API returned success=false")
                    if response_data.get("errors"):
                        print("Errors:")
                        for error in response_data.get("errors", []):
                            print(f"  - {error.get('description', 'Unknown error')}")
                    return False
                else:
                    print(f"✅ Folder Deleted Successfully!")
                    print(f"   - Folder ID: {folder_id}")
                    return True
        
        # If we get here without returning, something unexpected happened
        print(f"⚠️  Unexpected response format for deletion")
        return False