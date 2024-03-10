import unittest
from auto_artifacts.client.upload import upload_files
from auto_artifacts.client.download import download_file

class TestFileOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_upload_files(self):
        success = upload_files("http://192.168.150.11:8000", ["./resources/files_to_upload/file_3.txt"], "test", "sample_pw")
        self.assertTrue(success)
        pass

    def test_download_file(self):
        success = download_file("http://192.168.150.11:8000", "file_3.txt", "files_uploaded", "sample_pw")
        self.assertTrue(success)
        pass

if __name__ == "__main__":
    unittest.main()
