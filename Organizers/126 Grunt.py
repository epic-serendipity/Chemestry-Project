import os
import sqlite3
import tkinter
from tkinter.filedialog import askdirectory

# Set up the SQLite database
sql_file = sqlite3.connect('file_database.db')
c = sql_file.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY, unit TEXT, firstname TEXT, lastname TEXT, extension TEXT)''')

# Create the file selection GUI
root = tkinter.Tk()
root.withdraw()
folder_selected = askdirectory(title = "Select the folder containing the files ")

# Access the files in the folder
for filename in os.listdir(folder_selected):
    # Split the filename into its components
    filename_parts = filename.split("_")
    unit = filename_parts[0]
    firstname = filename_parts[1]
    lastname = filename_parts[2].split(".")[0]
    extension = filename_parts[2].split(".")[1]
    
    # Add the filename components to the SQL database
    c.execute("INSERT INTO files(unit, firstname, lastname, extension) VALUES(?,?,?,?)",
            (unit, firstname, lastname, extension))
    
    # Move the file into a subfolder based on the last name and unit
    file_path = os.path.join(folder_selected, filename)
    folder_name = unit + "/" + lastname
    new_folder_path = os.path.join(folder_selected, folder_name)
    # Check if the subfolder exists, otherwise create it
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    # Move the file into the subfolder
    new_file_path = os.path.join(new_folder_path, filename)
    if os.path.exists(new_file_path):
        # Move the file into the Duplicates folder if it already exists
        os.rename(file_path, os.path.join(folder_selected, "Duplicates", filename))
    else:
        os.rename(file_path, new_file_path)

# Commit and close the connection to the SQLite database
sql_file.commit()
sql_file.close()
