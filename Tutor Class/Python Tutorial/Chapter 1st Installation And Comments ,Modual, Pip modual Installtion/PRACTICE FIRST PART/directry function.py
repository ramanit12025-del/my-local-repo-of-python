import os
# select dicretory whose content you want to list  
directory = 'C:/Users/PC/Downloads/nothoing'

try:
    with os.scandir(directory) as it:#it is online os that provide directory list
        for entry in it:
            entry_type = "File" if entry.is_file() else "Directory" if entry.is_dir() else "Other"
            print(f"{entry_type}: {entry.name}")
except OSError as e:
    print(f"Error: {e}")
# next os for print the directory list
import os
# select dicretory whose content you want to list  
directory = '/'

contents = os.listdir(directory) #it is online os that provide directory list 

print(contents)
