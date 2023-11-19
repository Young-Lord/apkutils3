import os
import unittest

from apkutils3 import APK

# LOL you ctf guys do need this, but I don't care


class TestAPK(unittest.TestCase):
    def setUp(self):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "data", "test_zip_fake_pwd")
        )
        self.apk = APK(file_path)

    def test_get_manifest(self):
        self.apk.manifest_dict
        self.apk.manifest_object

    def test_get_strings(self):
        self.apk.strings

    def test_get_files(self):
        self.apk.files

    def test_get_opcodes(self):
        self.apk.opcodes


if __name__ == "__main__":
    print(
        "This is for CTF only and was removed in apkutils3. Use apkutils2 / apkutils instead."
    )
    exit(1)
    unittest.main()
