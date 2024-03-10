import unittest
import threading
import uvicorn
from fastapi import FastAPI
from auto_artifacts.server.app import app
from auto_artifacts.client.upload import upload_files
from auto_artifacts.client.download import download_file

import time

class TestFileOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the FastAPI server in a background thread
        cls.server_thread = threading.Thread(target=cls.run_server)
        cls.server_thread.start()
        time.sleep(1)  # Give the server a moment to start

    @classmethod
    def tearDownClass(cls):
        # Stop the FastAPI server
        # This might require a custom shutdown endpoint in your FastAPI app
        # Or a different mechanism to signal the server to stop
        pass

    @classmethod
    def run_server(cls):
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

    def test_upload_files(self):
        success = upload_files("http://127.0.0.1:8000", ["./resources/files_to_upload/file_2.txt"], "files_uploaded", "sample_pw")
        self.assertTrue(success)
        pass

    def test_download_file(self):
        success = download_file("http://127.0.0.1:8000", "file_2.txt", "files_uploaded", "sample_pw")
        self.assertTrue(success)
        pass

if __name__ == "__main__":
    unittest.main()
