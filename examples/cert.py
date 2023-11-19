import os

from apkutils3 import APK

file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "test")
)
apk = APK(file_path)

for item in apk.certs:
    print(item)
