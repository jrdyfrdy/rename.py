import os
import pandas as pd
import natsort

# Read directory of certificates 
folder = os.listdir('sscerts')

# Read CSV
df = pd.read_csv('names.csv')

# Loop through the length of the directory of certificates
for i in range(len(folder)):
    # Set num variable for the number found in filename (eg. 1.pdf as '1', 171.pdf as '171')
    num = folder[i].split('.')[0]

    # Convert num to int
    idx = int(num)

    # Set src variable for the source directory of the file
    src = f'sscerts/{folder[i]}'

    # Set dest variable for the destination directory of the file 
    dest = f"sscerts/{df['Names'][idx-1]}.pdf"

    # Rename files based on its directory
    os.rename(src, dest)
