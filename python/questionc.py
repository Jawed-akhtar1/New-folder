from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

# SharePoint site and authentication details
site_url = "https://yourcompany.sharepoint.com/sites/yoursite"
client_id = "your-client-id"
client_secret = "your-client-secret"
folder_url = "/sites/yoursite/Shared Documents/YourFolder"  # Relative URL of the folder in SharePoint

# File to upload
file_path = "C:\\path\\to\\your\\file.txt"
file_name = os.path.basename(file_path)

def upload_file_to_sharepoint(site_url, client_id, client_secret, folder_url, file_path):
    # Authenticate with SharePoint
    ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))
    
    # Get the folder where you want to upload the file
    folder = ctx.web.get_folder_by_server_relative_url(folder_url)
    
    with open(file_path, 'rb') as file_content:
        # Upload the file
        target_file = folder.upload_file(file_name, file_content).execute_query()
        print(f"File {target_file.serverRelativeUrl} has been uploaded successfully.")

# Run the upload function
upload_file_to_sharepoint(site_url, client_id, client_secret, folder_url, file_path)