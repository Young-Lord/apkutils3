import json
import os

from apkutils3 import APK

file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "test")
)
apk = APK(file_path)

m_xml = apk.orig_manifest
print(m_xml)

m_dict = apk.manifest_dict
print(json.dumps(m_dict, indent=4))

# get any item you want from dict
print("package:", m_dict["@package"])
print("android:versionName:", m_dict["@android:versionName"])
