import os
import shutil

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser(r'C:\Users\mh177\Downloads\old')


destination =  os.path.expanduser(r'C:\Users\mh177\Downloads\new')

# Define the destination folders for each file type


# Ensure the destination folders exist
def make_folder(folder):
    try:
        os.makedirs(os.path.join(destination, folder), exist_ok=True)
    except :
        pass
# Function to move files
def move_file(file_path, destination_folder):
    try:
        # shutil.move(file_path, destination_folder)
            shutil.copy2(file_path, destination_folder)

    except:
        pass
# Walk through all folders and files in the Downloads directory recursively
for root, dirs, files in os.walk(downloads_folder):
    for file in files:
        file_path = os.path.join(root, file)
        # file_extension = os.path.splitext(file)[0].lower()
        file_extension=file.split('.')[0]
        file_extension=file_extension.split()[0]
        print(file)
        make_folder(file_extension)


       
        destination_folder = os.path.join(destination, file_extension)
        move_file(file_path, destination_folder)
        

print("Files have been organized.")
