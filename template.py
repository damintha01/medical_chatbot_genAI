import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


list_of_files = [
    "app.py",
    "requirements.txt",
    "src/__init__.py",
    "src/helper.py",
    "src/prompts.py",
    ".env",
    "setup.py",
    "research/trials.ipynb"]

for file in list_of_files:
    file_path = os.path(file_path)
    filedir,filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created file: {file_path}")
