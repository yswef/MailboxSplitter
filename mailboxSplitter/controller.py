import tkinter as tk
from tkinter import filedialog
from time import sleep
import main

def splitter():
    # create a hidden window
    root = tk.Tk()
    root.withdraw()  # hide a tkinter window
    # open a window to choose the file
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Mail File", "*.mbox")])
    # verify if the user chooses a file
    if file_path: 
        print(f"Selected file: {file_path}")
        print("\033[1mchoose a folder:\033[0m")
        #The code will stop for two seconds
        sleep(2)
        #Choose a folder to save partitions
        output_dir = filedialog.askdirectory()
        # verify if the user chooses a file
        if output_dir:
            print(f"Selected folder: {output_dir}")
            #start splitter
            main.split_mbox(file_path,output_dir)
        else:
            print("No folder was selected.")
    else:
        print("No file was selected.")
    


def start():
    while True:
        print("[1]start splitter\n\n[0]exit")
        front = input("")
        if front == "1":
            splitter()
        elif front == "0":
            break
        else:
            print("\n\033[31mWrong choice, try again\033[0m\n")
            sleep(1)


