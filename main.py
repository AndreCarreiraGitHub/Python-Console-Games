import subprocess
import os

content = """0
0
0
"""

#Delete file so it resets the values from the previous time without corrupting the file
def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("File doesn't exist.")
     
#Recreate the file with the default values   
def create_and_write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' has been created and content has been written.")
    except Exception as e:
        print(f"Error: {e}")

delete_file("info.txt")
create_and_write_file("info.txt", content)
    
subprocess.run(["python", "mainmenu.py"])