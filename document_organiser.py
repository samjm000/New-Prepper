# document_organiser.py retrieve documents from parent directory
import os
import re
from datetime import datetime

def get_documents_in_order():
    #hardcoded target directory
    target_directory = (r"prepped clinics/")

    # Regex pattern to match the date in the filename
    pattern = re.compile(r"\d{2}\d{2}\d{2}")

    # Get list of all files in the directory
    files = os.listdir(target_directory)

    # Filter files based on whether they match the date pattern
    files_with_dates = [f for f in files if pattern.search(f)]

    # Sort the files by date
    files_with_dates.sort(
        key=lambda date: datetime.strptime(pattern.search(date).group(), "%d%m%y"),
        reverse=True,
    )

    # combine path with filenames
    for i in range(len(files_with_dates)):
        files_with_dates[i] = os.path.join(target_directory, files_with_dates[i])
        print(f"File {i+1} : {files_with_dates[i]}")
            
    # testing
    print(f"Found {len(files_with_dates)} clinic files")

    return files_with_dates

if __name__ == "__main__":
    print("Testing function get docs in order")
    get_documents_in_order()
