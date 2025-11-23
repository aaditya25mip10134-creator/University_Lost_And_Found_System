import csv
import os
import datetime
# Name of saved files"database" 
Record_book = "record_book.csv"

def initialize_system():
    if not os.path.exists(Record_book):
        with open(Record_book, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Aaditya singhal(developer)
            #  to Create the header row
            writer.writerow(["ID", "Status", "Item Name", "Description", "Location", "Date", "Contact"])

def report_item():
    print("\n--- REPORT AN ITEM ---")
    status = input("Is this item 'Lost' or 'Found'? (L/F): ").strip().upper()
    status = "LOST" if status == 'L' else "FOUND"
    
    name = input("Item Name (e.g., Blue Bottle): ")
    desc = input("Description (Color, Brand, distinct marks): ")
    loc = input(f"Location where it was {status.lower()}: ")
    contact = input("Your Contact Info (Phone/Room No): ")
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    item_id = 1
    if os.path.exists(Record_book):
        with open(Record_book, 'r') as f:
            item_id = sum(1 for line in f) 

    with open(Record_book, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([item_id, status, name, desc, loc, date_str, contact])
    
    print(f" Succesfully Item logged {status}.")

def search_items():
    """Module to search for items by keyword."""
    print("\n--- SEARCH REGISTRY ---")
    keyword = input("Enter a keyword to search (e.g., 'keys', 'cycle'): ").lower()
    
    found_match = False
    
    try:
        with open(Record_book, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            print(f"\n{'ID':<5} {'STATUS':<10} {'ITEM NAME':<20} {'LOCATION':<15} {'CONTACT'}")
            print("-" * 70)
            
            for row in reader:
                # Aaditya Singhal(developer)
                #  row[2] is Item Name, row[3] is Description
                # We check if keyword is in Name OR Description
                if keyword in row[2].lower() or keyword in row[3].lower():
                    print(f"{row[0]:<5} {row[1]:<10} {row[2]:<20} {row[4]:<15} {row[6]}")
                    found_match = True
    except FileNotFoundError:
        print("System empty. Record not found.")
        return

    if not found_match:
        print("No matches found.")

def delete_item():
    # Aaditya singhal(Developer)
    # Code is  to remove an item (Claimed/Returned)
    print("\n--- REMOVE/CLAIM ITEM ---")
    target_id = input("Enter Item Id to Remove: ")
    
    rows = []
    found = False
    
    try:
        with open(Record_book, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == target_id:
                    found = True 
                else:
                    rows.append(row)
        
        if found:
            with open(Record_book, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(" Item removed .")
        else:
            print("ID not found.")
            
    except FileNotFoundError:
        print("No records exist.")

def main():
    initialize_system()
    while True:
        print("\n=== HOSTEL LOST & FOUND SYSTEM ===")
        print("1. Report an Item (Lost/Found)")
        print("2. Search for an Item")
        print("3. Mark Item as Returned (Delete)")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            report_item()
        elif choice == '2':
            search_items()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
