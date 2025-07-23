import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

target_folder = os.path.expanduser("~/Downloads")

file_mappings = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents":[".doc", ".docx", ".txt", ".rtf"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "CAD": [".dwg", ".dxf", ".step", ".stp", ".iges", ".igs", ".sldprt", ".sldasm"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"]
}

def get_folder_name(extension, selected_categories):
    for folder, extensions in file_mappings.items():
        if extension.lower() in extensions and folder in selected_categories:
            return folder 
    return None

def organize_folder(folder, status_label, selected_categories):
    try:
        files_moved = 0
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                folder_name = get_folder_name(ext, selected_categories)
                
                if folder_name:
                    new_folder_path = os.path.join(folder, folder_name)
                    os.makedirs(new_folder_path, exist_ok = True)
                    shutil.move(file_path, os.path.join(new_folder_path, filename))
                    files_moved += 1
            
        status_label.config(text=f"Organized {files_moved} files.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong {e}")

def launch_gui():
    def browse_folder():
        folder = filedialog.askdirectory()
        if folder:
            folder_path.set(folder)
            status_label.config(text="Ready to organize!")
    
    def run_organizer():
        folder = folder_path.get()
        if not folder:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return
        
        selected = [cat for cat, var in check_vars.items() if var.get()]

        if not selected:
            messagebox.showwarning("No Categories", "Please select at least one file category.")
            return
        
        organize_folder(folder, status_label, selected)

    root = tk.Tk()
    root.title("Smart File Organizer")
    root.geometry("500x500")
    root.resizable(False, False)

    folder_path = tk.StringVar()

    tk.Label(root, text="Select folder to organize:", font=("Arial", 12)).pack(pady=10)
    tk.Entry(root, textvariable=folder_path, width=40).pack()
    tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
    
    tk.Label(root, text="Select categories to organize:", font=("Arial", 12, "bold")).pack(pady=10)

    check_vars = {}
    for category in file_mappings.keys():
        var = tk.BooleanVar(value=False)
        check_vars[category] = var
        tk.Checkbutton(root, text=category, variable=var).pack(anchor="w", padx=20)

    tk.Button(root, text="Organize Files", command=run_organizer, bg="#4CAF50", fg="white").pack(pady=20)

    status_label = tk.Label(root, text="", font=("Arial", 10))
    status_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
    