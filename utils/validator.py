# utils/validator.py

def validate_http_status(response, expected_statuses):
    """Validate if the response status code matches expected (can be a list)"""
    if isinstance(expected_statuses, int):
        expected_statuses = [expected_statuses]
    
    if response.status_code not in expected_statuses:
        print(f"❌ ERROR: Expected status {expected_statuses}, got {response.status_code}")
        return False
    print(f"✅ Status Code Validated: {response.status_code}")
    return True


def validate_response_structure(response_data, required_keys):
    """Manually validate if response contains required keys"""
    if not isinstance(response_data, dict):
        print("❌ ERROR: Response is not a dictionary")
        return False
    
    missing_keys = []
    for key in required_keys:
        if key not in response_data:
            missing_keys.append(key)
    
    if missing_keys:
        print(f"❌ ERROR: Missing required keys: {missing_keys}")
        return False
    
    print(f"✅ Response Structure Validated: All required keys present")
    return True


def validate_api_success(response_data):
    """Validate if API returned success=true"""
    if not response_data.get("success"):
        print("❌ API returned success=false")
        if response_data.get("errors"):
            print("Errors:")
            for error in response_data.get("errors", []):
                print(f"  - {error.get('description', 'Unknown error')}")
        return False
    return True