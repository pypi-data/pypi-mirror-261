import os
import requests

def upload_files(base_url, file_paths, path, password):
    """
    Uploads files to the FastAPI server.

    Args:
        base_url (str): The base URL where the FastAPI server is running.
        file_paths (list of str): List of file paths of the files to be uploaded.
        path (str): The path where the files should be uploaded on the server.
        password (str): The password for accessing the upload functionality.

    Returns:
        bool: True if the files were uploaded successfully, False otherwise.
    """

    # The URL for the upload endpoint
    url = f"{base_url}/artifacts/upload/files"

    # Prepare the files for uploading
    files = [('files', (open(file_path, 'rb'))) for file_path in file_paths]

    # Data to be sent in the form
    data = {
        'path': path,
        'pw': password,
    }

    # Make the POST request to upload the files
    response = requests.post(url, files=files, data=data)

    if response.ok:
        # If the request was successful, return True
        print(response.json())  # Optionally print the response from the server
        return True
    else:
        # If there was an error, print the error and return False
        print(f"Error uploading files: {response.text}")
        return False
