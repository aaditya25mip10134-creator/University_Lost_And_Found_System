# 🎒 University Lost & Found Registry

> **A Python-based solution to organize the chaos of lost items on campus.**

### 📖 Overview
We've all been there—losing an ID card in the cafeteria or finding a stray set of keys in the hallway. Currently, retrieving these items involves scrolling through endless WhatsApp groups or checking messy notice boards.

The **University Lost & Found Registry** is a CLI (Command Line Interface) tool designed to fix this. It provides a centralized, digital log where students can report missing items, register found objects, and search for them instantly. It replaces the "needle in a haystack" search with a simple, persistent database.

---

### ✨ Key Features

* **📝 Report & Log:** Users can easily record details about lost or found items, including location, physical description, and contact information.
* **🔎 Smart Search:** Includes a case-insensitive keyword search (e.g., searching for "wallet" will also find "Black Leather Wallet").
* **💾 Data Persistence:** Unlike a simple script that forgets data when closed, this program uses **File I/O (CSV)** to ensure records are saved permanently.
* **✅ Claim & Resolve:** Once an item is returned to its rightful owner, the entry can be officially removed from the database to keep the registry clean.

---

### 🛠️ Tech Stack & Concepts

This project was built to demonstrate core Python programming concepts, connecting theory with a real-world application.

* **Language:** Python 3.x
* **Libraries:**
    * `csv`: For handling the database operations.
    * `datetime`: For timestamping entries.
    * `os`: For file verification and system compatibility.
* **Core Concepts Applied:**
    * Modular Programming (Top-Down Design)
    * File Handling (Read/Write/Append)
    * String Manipulation
    * Exception Handling (Error management)

---

### 📂 Project Structure

The code follows a **Top-Down Modular Design** approach to ensure readability and easy maintenance:

| Module / Function | Description |
| :--- | :--- |
| **`initialize_system()`** | Checks system health. If the CSV database doesn't exist, it creates a new one with headers. |
| **`report_item()`** | Captures user input (Lost/Found details) and securely writes it to the database file. |
| **`search_items()`** | Reads the file and filters data based on user keywords to find matches. |
| **`delete_item()`** | Handles the logic for closing cases (removing items that have been claimed). |

---

### 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/lost-and-found-registry.git](https://github.com/your-username/lost-and-found-registry.git)
    ```
2.  **Navigate to the project folder:**
  
  code.py
  
3.  **Run the script:**
    ```bash
    python main.py
    ```
    *(Note: Ensure you have Python installed on your system).*

---
