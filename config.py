import shutil

file_path = "info.txt"

#Change values in specific line in info.txx
def change_line(file_path, line_number, new_content):
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Check if the line number is valid
        if line_number > len(lines) or line_number < 1:
            return f"Error: The file has only {len(lines)} lines."
        
        # Modify the specific line
        lines[line_number - 1] = new_content + '\n'
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        return f"Line {line_number} has been modified."
    
    except FileNotFoundError:
        return "Error: File not found."
    
    except FileNotFoundError:
        return "Error: File not found."

#Read specific line to get the results from info.txt
def read_specific_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            for current_line_number, line in enumerate(file, start=1):
                if current_line_number == line_number:
                    return line.strip()  # Remove leading/trailing whitespace
    except FileNotFoundError:
        return None
    
win = int(read_specific_line(file_path, 1))
lose = int(read_specific_line(file_path, 2))
turn = int(read_specific_line(file_path, 3))

#Setting up colours
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

#Get console width
columns, _ = shutil.get_terminal_size()
#Create a line that spans the width of the screen
line = '_' * columns