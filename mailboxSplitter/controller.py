import tkinter as tk
from tkinter import filedialog
from time import sleep
from mailboxSplitter import main
import os

def splitter():
    # create a hidden window
    root = tk.Tk()
    root.withdraw()  # hide a tkinter window
    # open a window to choose the file
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Mail File", "*.mbox")])
    # verify if the user chooses a file
    if file_path: 
        print(f"Selected file: {file_path}")
        print("\033[1mChoose a folder:\033[0m")
        #The code will stop for two seconds
        sleep(2)
        #Choose a folder to save partitions
        output_dir = filedialog.askdirectory()
        # verify if the user chooses a file
        if output_dir:
            print(f"Selected folder: {output_dir}")
            files = os.path.getsize(file_path)
            print(f"The file will be cut to {int(files/(50*1024*1024)) + 1} files")
            #start splitter
            main.split_mbox(file_path,output_dir)
        else:
            print("No folder was selected.")
    else:
        print("No file was selected.")
    


def start():
    while True:
        print("[1]Start splitter\n\n[0]Exit")
        front = input("Choose:\n")
        if front == "1":
            splitter()
        elif front == "0":
            break
        else:
            print("\n\033[31mWrong choice, try again\033[0m\n")
            sleep(1)


