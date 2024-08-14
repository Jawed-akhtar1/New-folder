import requests

def download_file(url, file_name):
    # Send a GET request to the server to download the file
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in binary mode and write the contents
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"File '{file_name}' downloaded successfully!")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Example usage
url = "https://play-lh.googleusercontent.com/L6qehUCLcgG7W3cH1aBel04XKSp5GA9oX3NrUWgwaIwkiYWnhF-xJftIQz5m5Uy-0K67"  # Replace with the actual URL of the file you want to download
file_name = "downloaded_file.zip"  # Replace with the desired file name

download_file(url, file_name)
