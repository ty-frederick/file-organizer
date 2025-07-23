import os
import shutil

target_folder = os.path.expanduser("~/Downloads")

file_mappings = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents":[".doc", ".docx", ".txt", ".rtf"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def get_folder_name(extension):
    for folder, extensions in file_mappings.items():
        if extensions.lower() in extensions:
            return folder 
    return "Other"

def organize_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            folder_name = get_folder_name(ext)
            new_folder_path = os.path.join(folder, folder_name)

            os.makedirs(new_folder_path, exist_ok = True)
            shutil.move(file_path, os.path.join(new_folder_path, filename))
            print(f"Moved: {filename} -> {folder_name}/")

        if __name__ == "__main__":
            print(f"Organizing folder: {target_folder}")
            organize_folder(target_folder)
            print("Done!")
        