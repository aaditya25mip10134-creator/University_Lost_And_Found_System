# University_Lost_And_Found_System
 A Python-based CLI (Command Line Interface) program called the University Lost & Found Registry was created to make it easier to report and retrieve misplaced objects on a university campus or in a dorm.

 This initiative offers a centralized, durable digital log where students can report missing items, register found objects, and search the database using keywords, replacing disorganized manual notices and chat groups.
 Important Features 📝 Report things: Users can record information about lost or found things, such as their location, description, and contact data.

🔎 Smart Search: Users can locate products with ease using case-insensitive keyword search (e.g., searching "bag" finds "Blue Bag").

💾 Data Persistence: Ensures data is saved even after the program ends by using File I/O (CSV).

✅ Claim & Resolve: After an object is returned to its owner, it can be removed from the database.

🛠️ Tech Stack Language: Python 3.x

Modules utilized include datetime (timestamping), os (file verification), and csv (database processing).

Modular programming, file handling, string manipulation, and exception handling are among the concepts used.

📂 Project Organization
 The project employs a Top-Down Modular Design methodology:

 initialize_system(): If the CSV database doesn't already exist, it is set up.

 report_item() publishes data to the file and manages user input.

 search_items(): This function reads the file and uses user queries to filter data.

 delete_item(): Manages the reasoning behind removing or claiming cases that have been resolved.
