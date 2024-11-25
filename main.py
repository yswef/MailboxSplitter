# # *Script to Split by Email Co
import os 

def split_mbox(input_file, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir) 
    # This line reads the file with 'utf-8' encoding, and any reading errors are ignored.
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        
            file_count = 1
            current_file = open(os.path.join(output_dir, f'part-{file_count}.mbox'), 'w', encoding='utf-8', errors='ignore') 

            for line in f:
                file_size = os.path.getsize(f"{output_dir}/part-{file_count}.mbox")#file size
                # print(f"{file_size}")
                if file_size > 52428000:
                    print("done")
                    current_file.close()
                    file_count = file_count + 1
                    current_file = open(os.path.join(output_dir, f'part-{file_count}.mbox'),'w', encoding='utf-8', errors='ignore')
                current_file.write(line) 
                
            current_file.close()
            print("split comblet")
            
        

# Example usage:
split_mbox('Inbox.mbox', 'split5') # Split every 50 MG

# # Replace 'largefile.mbox' with your file name and adjust 1000 to the number of emails per file.split/part-1.mbox