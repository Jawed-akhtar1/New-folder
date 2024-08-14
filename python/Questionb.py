
import os
import requests
import zipfile
from io import BytesIO

# Define the download URL and destination folder
download_url = "https://play-lh.googleusercontent.com/L6qehUCLcgG7W3cH1aBel04XKSp5GA9oX3NrUWgwaIwkiYWnhF-xJftIQz5m5Uy-0K67"  # Replace with your download URL
download_folder = "C:\\Download Folder"
extract_folder = "C:\\Extract Folder"

# Ensure download and extract directories exist
os.makedirs(download_folder, exist_ok=True)
os.makedirs(extract_folder, exist_ok=True)

def download_file(url, download_path):
    # Send a HTTP request to the server and download the file
    response = requests.get(url)
    response.raise_for_status()  # Check if the download was successful

    # Save the file to the specified path
    with open(download_path, "wb") as file:
        file.write(response.content)

    return download_path

def extract_zip_file(zip_path, extract_to):
    # Extract the ZIP file to the specified directory
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main(url):
    # Get the file name from the URL
    file_name = os.path.basename(url)
    download_path = os.path.join(download_folder, file_name)

    # Download the file
    print(f"Downloading {file_name}...")
    downloaded_file = download_file(url, download_path)
    print(f"Downloaded {downloaded_file}")
    print("Extraction successfully")

    # Check if the downloaded file is a ZIP file
    if zipfile.is_zipfile(downloaded_file):
        # Create a folder with the same name as the ZIP file in the extract folder
        extract_to = os.path.join(extract_folder, os.path.splitext(file_name)[0])
        os.makedirs(extract_to, exist_ok=True)

        # Extract the ZIP file
        print(f"Extracting {file_name} to {extract_to}...")
        extract_zip_file(downloaded_file, extract_to)
        print(f"Extraction complete!")

if __name__ == "__main__":
    main(download_url)


