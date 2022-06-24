import wmi
import os
from pathlib import Path
import shutil
import glob

# determine the usb letter
c = wmi.WMI ()
for drive in c.Win32_LogicalDisk ():
    if(drive.Description == 'Removable Disk'):
        usb_letter = drive.Caption
       
# defining source and destination paths
src = "C:\\Users\\Abdallah\\Desktop"
dst = f"{usb_letter}\\"

# defining extension files to transfer
exts = ['pdf','docx','txt','png','jpeg','jpg','exe']

for ext in exts:
    #listeing all files with specific extension
    files = glob.iglob(os.path.join(src, f"*.{ext}"))
    for fname in files:
    # copying the files in root directory to the destination directory
        shutil.copy2(os.path.join(src, fname), dst)

