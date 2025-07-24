# File Organizer

A Python-based desktop application that helps you keep your folders tidy by automatically organizing files into categories based on file type. The app features a user-friendly interface for selecting a folder to organize and choosing which categories to sort into.

## Features

- 📁 **Custom folder selection** — Choose the directory you want to organize.
- ✅ **Selective sorting** — Pick which file categories (Documents, Code, CAD, Spreadsheets, etc.) to sort into.
- 🖱️ **GUI interface** — Built with tkinter for simple interaction.
- 🚀 **Quick setup** — No configuration files or databases required.

## Technologies Used

- Python 3
- `tkinter` for the graphical user interface
- `os` and `shutil` for file management
- Packaged into an executable using PyInstaller

## Motivation

I created this project to better understand how users interact with code and what it takes to build a user-friendly interface. At the same time, I wanted to solve a real personal problem — keeping my workspaces and folders clean and organized.

## How It Works

1. Launch the app.
2. Select the folder you want to organize.
3. Choose which types of files you want to sort (e.g., only Documents and CAD).
4. The app will create subfolders (if they don’t exist) and move matching files accordingly.

## Future Improvements

- Drag-and-drop folder selection
- Remembering user preferences
- Integration with cloud storage (e.g., OneDrive, Google Drive)

## Getting Started

To run the code:

```bash
python main.py
