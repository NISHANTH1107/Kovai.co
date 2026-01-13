# api/client.py
import requests
import json
from config.settings import get_headers
from utils.logger import log_request, log_response
from utils.validator import validate_http_status, validate_response_structure, validate_api_success

class APIClient:
    def __init__(self, base_url, api_token=None):
        self.base_url = base_url
        self.headers = get_headers(api_token)
        self.api_token = api_token
    
    def update_api_token(self, api_token):
        """Update API token in headers"""
        self.api_token = api_token
        self.headers = get_headers(api_token)
    
    def _make_request(self, method, endpoint="", data=None, expected_status=None, timeout=30):
        """Generic request method"""
        url = f"{self.base_url}{endpoint}" if endpoint else self.base_url
        
        try:
            # Log the request
            log_request(method, url, self.headers, data)
            
            # Make the request
            if method.upper() == "GET":
                response = requests.get(url, headers=self.headers, timeout=timeout)
            elif method.upper() == "POST":
                response = requests.post(url, headers=self.headers, json=data, timeout=timeout)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=self.headers, json=data, timeout=timeout)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=self.headers, timeout=timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            # Log the response
            log_response(response)
            
            # Validate status code if expected_status is provided
            if expected_status:
                if not validate_http_status(response, expected_status):
                    return None
            
            # Parse response if there's content
            if response.text:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    return {"raw_response": response.text, "status_code": response.status_code}
            else:
                return {"status_code": response.status_code}
                
        except requests.exceptions.Timeout:
            print(" ERROR: Request timeout after 30 seconds")
            return None
        except requests.exceptions.RequestException as e:
            print(f" ERROR: Request failed: {e}")
            return None
        except Exception as e:
            print(f" ERROR: Unexpected error: {e}")
            return None