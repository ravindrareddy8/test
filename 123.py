#1 Hello world
print("Hello, World!")
#2 Basic file handling
with open('example.txt', 'w') as file:
    file.write('This is sample script!')
#3 working with command line
#Learn to create scripts that accept input and arguments from the command line using the sys and argparse modules.
#Example using sys:
import sys
if len(sys.argv) > 1:
    print(f"Hello,{sys.argv{1}}!")
else:
    print("Hello, World!")
#4 Example using argparse
import argparse

parser = argparse.ArgumentParser(description='A simple script.')
parser.add_argument('name', hepl='Your name')
args(f"Hello, {args.name}!")
#5. File and Directory Manipulation
#Read and Write Files
with open ('example.txt', 'r') as file:
    contents = file.read()
    print (contents)
#Directory Manipulation
import os
os.mkdir('new_directory')
os.chdir('new_directory')
#6. Automating System Tasks
#Use the os and subprocess modules to run system commands:
Run System Commands:
python
Copy code
import os
os.system('ls')  # For Linux/macOS, use 'dir' for Windows
Run Commands Using subprocess:
python
Copy code
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
7. Scheduling and Task Automation
You can write scripts that automate tasks like backups or file organization:

Use Python’s time module to add delays or schedule periodic tasks.
For regular scheduling on Linux, use cron jobs, and on Windows, use Task Scheduler.
8. Use Python Libraries for Advanced Scripting
There are many libraries to simplify and extend scripting:

Pathlib: Easier file and directory handling.
python
Copy code
from pathlib import Path
Path('new_file.txt').write_text('Hello, World!')
shutil: File operations like copying, moving, and removing.
python
Copy code
import shutil
shutil.copy('source.txt', 'destination.txt')
os: For more advanced system operations (like environment variables).
9. Error Handling and Logging
Include error handling to make your scripts robust:

Try/Except Blocks:
python
Copy code
try:
    with open('non_existent_file.txt', 'r') as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found!")
Logging: Track script execution with logs using the logging module.
python
Copy code
import logging
logging.basicConfig(filename='script.log', level=logging.DEBUG)
logging.debug('This is a debug message')
10. Practice with Real-World Projects
Automate File Backups: Write a script to back up important files.
Data Parsing: Write scripts to parse CSV files, XML, or JSON.
Web Scraping: Use libraries like BeautifulSoup and requests to scrape websites for data.
Batch Renaming Files: Write a script to rename files in bulk.
11. Optimize and Refactor
As you get comfortable, work on optimizing your scripts and making them more efficient. Learn about:

List comprehensions for cleaner loops.
Modularizing code into functions or classes.
12. Version Control with Git
As your scripts grow more complex, learn version control using Git to keep track of changes and collaborate on code.

Tools to Help You Learn Python Scripting:
IDE: Use VS Code or PyCharm for scripting.
Cheat Sheets: Download Python cheat sheets to quickly refer to common syntax.
Community Support: Use forums like Stack Overflow to troubleshoot errors.
Conclusion:
Start small with automating simple tasks, practice regularly, and slowly work on more complex scripts. Scripting is a powerful way to automate repetitive tasks and streamline workflows!








