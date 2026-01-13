# utils/logger.py
import json

def log_request(method, url, headers, body=None):
    """Log the outgoing request details"""
    print("\n" + "="*80)
    print(f"REQUEST: {method} {url}")
    print("-"*80)
    print("Headers:")
    for key, value in headers.items():
        # Mask the token for security
        if key.lower() == "api_token":
            print(f"  {key}: {'*' * 10}{value[-4:] if value else '****'}")
        else:
            print(f"  {key}: {value}")
    
    if body:
        print("\nRequest Body:")
        print(json.dumps(body, indent=2))
    print("="*80)


def log_response(response):
    """Log the incoming response details"""
    print("\n" + "-"*80)
    print(f"RESPONSE: {response.status_code} {response.reason}")
    print("-"*80)
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    
    print("\nResponse Body:")
    try:
        # Try to parse as JSON and pretty print
        response_data = response.json()
        print(json.dumps(response_data, indent=2))
    except json.JSONDecodeError:
        print(response.text)
    print("-"*80 + "\n")