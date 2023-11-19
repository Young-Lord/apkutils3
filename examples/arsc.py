import os
import xmltodict
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from apkutils3 import APK
from apkutils3.consts import RESOURCE_XMLTODICT_FORCE_LIST

file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "test")
)
apk = APK(file_path)

package = apk.manifest_dict.get("@package", None)
if not package:
    exit()

icon_id = apk.manifest_dict.get("application", {}).get("@android:icon", None)
if not icon_id:
    exit()

icon_id = icon_id[1:].lower()
datas = xmltodict.parse(
    apk.arsc.get_public_resources(package),
    force_list=(RESOURCE_XMLTODICT_FORCE_LIST),
)


def get_icon_path():
    for item in datas["resources"]["public"]:
        if icon_id not in item.get("@id"):
            break
        return (item.get("@type"), item.get("@name"))


icon = get_icon_path()
assert icon
for item in apk.files:
    name = item.get("name")
    if icon[0] in name and icon[1] in name:
        print(name)
