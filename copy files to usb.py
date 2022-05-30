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
src = r"C:\Users\Abdallah\Desktop"
# src = r"G:\\"
dst = f"{usb_letter}\\"


exts = ['pdf','docx','txt','png','jpeg','exe']

for ext in exts:
    #listeing all files with specific extension
    files = glob.iglob(os.path.join(src, f"*.{ext}"))
    for fname in files:
    # copying the files in root directory to the destination directory
        # shutil.copy2(os.path.join(src, fname), dst)
    # copying the files in root directory and sub directories to the destination directory
        shutil.copytree(os.path.join(src, fname), dst)
