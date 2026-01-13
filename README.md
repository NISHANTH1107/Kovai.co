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

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd document360-drive-api
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

### Get All Folders
```bash
python tasks/get_folders.py
```

### Create a Folder
```bash
python tasks/create_folder.py
```

### Update a Folder
Edit `update_folder.py` with a folder ID, then run:
```bash
python tasks/update_folder.py
```

### Delete a Folder
Edit `delete_folder.py` with a folder ID, then run:
```bash
python tasks/delete_folder.py
```

---

## Sample Output

**GET folders:**
```
200
{ "success": true, "data": [...] }
```

**POST create:**
```
201
{ "success": true, "data": { "id": "...", "title": "nishanth-test" } }
```

---

## Notes

- Some folders in Document360 are system folders and cannot be deleted or renamed.
- The API returns proper error messages for such cases.

---

## Author
Nishanth
