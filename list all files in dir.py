# list all files end with .txt in download folder 
import os
from pathlib import Path
downloads = Path.home() / "Downloads"
for files in downloads.iterdir():
    if files.is_file() and files.suffix == ".txt":
        print(files.name)