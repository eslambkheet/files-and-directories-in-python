# list all pdf files and count it  
import os
from pathlib import Path
downloads = Path.home() / "Downloads"
count = 0
for files in downloads.iterdir():
    if files.is_file() and files.suffix == ".pdf":
        print(count , files.name)
        count += 1
