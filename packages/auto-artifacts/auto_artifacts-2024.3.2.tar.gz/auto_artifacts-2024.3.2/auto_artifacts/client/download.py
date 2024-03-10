import requests

def download_file(base_url, filename, path, password=None):
    """
    Downloads a file from the FastAPI server.

    Args:
        base_url (str): The base URL where the FastAPI server is running.
        filename (str): The name of the file to download.
        path (str): The path to the file, relative to the base path on the server.
        password (str, optional): The password for accessing private files. Defaults to None.

    Returns:
        bool: True if the file was downloaded successfully, False otherwise.
    """
    # Construct the full URL for the download endpoint
    url = f"{base_url}/download/file"

    # Parameters to be sent in the query string
    params = {
        'filename': filename,
        'path': path,
    }

    # Include the password in the parameters if it's provided
    if password is not None:
        params['pw'] = password

    # Make the GET request to download the file
    response = requests.get(url, params=params)

    if response.ok:
        # If the request was successful, save the file
        with open(filename, 'wb') as file:
            file.write(response.content)
        return True
    else:
        # If there was an error (e.g., file not found, authentication error), print the error and return False
        print(f"Error downloading file: {response.text}")
        return False
