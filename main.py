# main.py
import time
from config.settings import HEADERS, GlobalState
from tasks.get_folders import execute_task1
from tasks.create_folder import execute_task2
from tasks.update_folder import execute_task3
from tasks.delete_folder import execute_task4


def get_user_input(prompt, allow_empty=False):
    """Get input from user with validation"""
    while True:
        user_input = input(prompt).strip()
        if user_input or allow_empty:
            return user_input
        print("❌ Input cannot be empty. Please try again.")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*80)
    print("API TESTING MENU")
    print("="*80)
    print("1. Task #1: GET All Drive Folders")
    print("2. Task #2: POST Create a New Folder")
    print("3. Task #3: PUT Update Folder Name")
    print("4. Task #4: DELETE the Folder")
    print("5. Run All Tasks Sequentially")
    print("6. Exit")
    print("="*80)


def main():
    """Main execution flow"""
    print("\n" + "🚀 Welcome to API Testing Script")
    print("="*80)
    
    # Get API token from user
    api_token = get_user_input("Enter your API token: ")
    HEADERS["api_token"] = api_token
    
    print("\n✅ API Token configured successfully!")
    
    while True:
        display_menu()
        choice = get_user_input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            # Task 1: Get all folders
            folders = execute_task1(api_token)
            if folders is None:
                print("❌ Failed to retrieve folders.")
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            # Task 2: Create a new folder
            print("\n--- Create New Folder ---")
            folder_title = get_user_input("Enter folder title: ")
            parent_id = get_user_input("Enter parent folder ID (press Enter to skip for root level): ", allow_empty=True)
            
            created_folder = execute_task2(folder_title, parent_id if parent_id else None, api_token)
            if created_folder is None:
                print("❌ Failed to create folder.")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            # Task 3: Update folder name
            print("\n--- Update Folder Title ---")
            
            # Check if we have a stored folder ID
            stored_folder_id = GlobalState.get_created_folder_id()
            if stored_folder_id:
                print(f"Last created folder ID: {stored_folder_id}")
                use_stored = get_user_input("Use this folder ID? (y/n): ").lower()
                if use_stored == 'y':
                    folder_id = stored_folder_id
                else:
                    folder_id = get_user_input("Enter folder ID to update: ")
            else:
                folder_id = get_user_input("Enter folder ID to update: ")
            
            new_title = get_user_input("Enter new folder title: ")
            
            updated_folder = execute_task3(folder_id, new_title, api_token)
            if updated_folder is None:
                print("❌ Failed to update folder.")
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            # Task 4: Delete folder
            print("\n--- Delete Folder ---")
            
            # Check if we have a stored folder ID
            stored_folder_id = GlobalState.get_created_folder_id()
            if stored_folder_id:
                print(f"Last created folder ID: {stored_folder_id}")
                use_stored = get_user_input("Use this folder ID? (y/n): ").lower()
                if use_stored == 'y':
                    folder_id = stored_folder_id
                else:
                    folder_id = get_user_input("Enter folder ID to delete: ")
            else:
                folder_id = get_user_input("Enter folder ID to delete: ")
            
            confirm = get_user_input(f"Are you sure you want to delete folder {folder_id}? (y/n): ").lower()
            if confirm == 'y':
                deletion_success = execute_task4(folder_id, api_token)
                if not deletion_success:
                    print("❌ Failed to delete folder.")
                else:
                    # Clear the stored ID if we deleted it
                    if stored_folder_id and folder_id == stored_folder_id:
                        GlobalState.clear_created_folder_id()
            else:
                print("❌ Deletion cancelled.")
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            # Run all tasks sequentially
            print("\n--- Running All Tasks Sequentially ---")
            
            # Task 1: Get all folders
            folders = execute_task1(api_token)
            if folders is None:
                print("❌ Failed to retrieve folders. Stopping execution.")
                input("\nPress Enter to continue...")
                continue
            
            time.sleep(1)
            
            # Task 2: Create a new folder
            print("\n--- Create New Folder ---")
            folder_title = get_user_input("Enter folder title: ")
            parent_id = get_user_input("Enter parent folder ID (press Enter to skip for root level): ", allow_empty=True)
            
            created_folder = execute_task2(folder_title, parent_id if parent_id else None, api_token)
            if created_folder is None:
                print("❌ Failed to create folder. Stopping execution.")
                input("\nPress Enter to continue...")
                continue
            
            time.sleep(1)
            
            # Task 3: Update the folder name
            stored_folder_id = GlobalState.get_created_folder_id()
            if stored_folder_id:
                print("\n--- Update Folder Title ---")
                new_title = get_user_input(f"Enter new title for folder (current: {folder_title}): ")
                
                updated_folder = execute_task3(stored_folder_id, new_title, api_token)
                if updated_folder is None:
                    print("❌ Failed to update folder.")
            else:
                print("❌ No folder ID available for update.")
            
            time.sleep(1)
            
            # Task 4: Delete the folder
            if stored_folder_id:
                print("\n--- Delete Folder ---")
                confirm = get_user_input(f"Delete the created folder {stored_folder_id}? (y/n): ").lower()
                if confirm == 'y':
                    deletion_success = execute_task4(stored_folder_id, api_token)
                    if not deletion_success:
                        print("❌ Failed to delete folder.")
                    else:
                        GlobalState.clear_created_folder_id()
                else:
                    print("❌ Deletion skipped.")
            else:
                print("❌ No folder ID available for deletion.")
            
            print("\n" + "="*80)
            print("✅ All Tasks Completed!")
            print("="*80)
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            print("\n👋 Exiting API Testing Script. Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()