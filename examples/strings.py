import binascii
import os

from apkutils3 import APK

file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "test")
)
apk = APK(file_path)

orig_strs = apk.orig_strings  # the strings from all of classes\d*.dex
for item in orig_strs:
    if b"helloword" in item:
        print(item)

strs = apk.strings  # the strings from all of classes\d*.dex
for item in strs:
    s = binascii.unhexlify(item).decode("utf-8", errors="ignore")
    if "helloword" in s:
        print(s)

result = apk.strings_refx
for clsname in result:
    for mtdname in result[clsname]:
        if b"hellojni" in result[clsname][mtdname]:
            print(clsname, mtdname, result[clsname][mtdname])
