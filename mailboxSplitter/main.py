#  *Script to Split by Email Co
import os 
from time import sleep



def split_mbox(input_file, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir) 
        l = 0  
    # This line reads the file with 'utf-8' encoding, and any reading errors are ignored.
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            file_count = 1
            path = os.path.join(output_dir, f'part-{file_count}.mbox')
            current_file = open(path, 'w', encoding='utf-8', errors='ignore') 

            for line in f:
                file_size = os.path.getsize(path)#file size
                # print({file_size} )
                if file_size >= 52428000:
                    current_file.close()
                    file_count = file_count + 1
                    path = os.path.join(output_dir, f'part-{file_count}.mbox')
                    current_file = open(path, 'w', encoding='utf-8', errors='ignore')
                current_file.write(line)
                print(f"\033[1mWaiting{"."*l}\U0001F680   " , end="\r\033[0m")
                l += 1
                if l == 6:
                    l = 0
            current_file.close()
            print("split comblet")
            

# Example usage:
# split_mbox('largefile.mbox', 'split5') # Split every 50 MG

# # Replace 'largefile.mbox' with your file name and adjust 1000 to the number of emails per file.split/part-1.mbox