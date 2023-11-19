# apkutils [![PyPI version](https://badge.fury.io/py/apkutils-patch.svg)](https://badge.fury.io/py/apkutils-patch) [![GitHub license](https://img.shields.io/github/license/mikusjelly/apkutils-patch.svg)](https://github.com/mikusjelly/apkutils-patch/blob/master/LICENSE)

A library that gets infos from APK.

## Install and Test

```shell
pip install apkutils3
```

## Usage

```shell
$ python3 -m apkutils -h
usage: apkutils [-h] [-m] [-s] [-f] [-c] [-V] p

positional arguments:
  p              path

optional arguments:
  -h, --help     show this help message and exit
  -m             Show manifest
  -s             Show strings
  -f             Show files
  -c             Show certs
  -V, --version  show program's version number and exit
```

GUI tool

```shell
$ python -m apkutils.gui
# Click Bind
```

Right click an `*.apk` file. Select `APK Parser`. You will see

![Img](imgs/apk-parser.png)

## Reference

- apkutils\axml from [mikusjelly/axmlparser](https://github.com/mikusjelly/axmlparser) ![Project unmaintained](https://img.shields.io/badge/project-unmaintained-red.svg)
- apkutils\dex from [google/enjarify](https://github.com/google/enjarify)
- Original projects: [apkutils2](https://github.com/codeskyblue/apkutils2), [apkutils](https://github.com/kin9-0rz/apkutils), license under MIT License.
