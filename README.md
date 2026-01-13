# Document360 Drive API Testing

## Overview
This project demonstrates how to interact with the Document360 Drive API using Python.
It covers all required CRUD operations:

- GET all folders
- POST create a folder
- PUT update a folder
- DELETE a folder

The project follows the API authentication requirement using the `api_token` header.

---

## Tech Stack
- Python 3.10+
- requests
- python-dotenv

---

## Project Structure

```
document360-drive-api/
│
├── .env                      # Environment variables (API_TOKEN, USER_ID, BASE_URL)
├── .env.example             # Example environment file
├── requirements.txt         # Python dependencies
├── main.py                  # Main menu-driven interface
├── README.md               # This file
│
├── config/                  # Configuration module
│   ├── __init__.py
│   └── settings.py         # API configuration and global state
│
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── logger.py          # Request/response logging
│   └── validator.py       # Response validation
│
├── api/                    # API client module
│   ├── __init__.py
│   └── client.py          # Base API client with request methods
│
└── tasks/                  # Individual task implementations
    ├── __init__.py
    ├── task1_get_folders.py    # GET all folders
    ├── task2_create_folder.py  # POST create folder
    ├── task3_update_folder.py  # PUT update folder
    ├── task4_delete_folder.py  # DELETE folder
    └── get_folders.py          # (Legacy) Simple GET task
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd Kovai.co
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Copy `.env.example` and fill in your credentials:

```env
API_TOKEN=your_document360_token
USER_ID=your_user_id
```

---

## Running the API Tasks

Each API operation is placed in a separate file inside `tasks/`.

### Run the Complete Project
```bash
python main.py
```
---

## Sample Output

```
Welcome to API Testing Script
====================================================================================================

 API Token configured successfully!

====================================================================================================
API TESTING MENU
====================================================================================================
1. Task #1: GET All Drive Folders
2. Task #2: POST Create a New Folder
3. Task #3: PUT Update Folder Name
4. Task #4: DELETE the Folder
5. Exit
====================================================================================================

Enter your choice (1-5):
```

---

## Notes

- Some folders in Document360 are system folders and cannot be deleted or renamed.
- The API returns proper error messages for such cases.

---

## Author
Nishanth
