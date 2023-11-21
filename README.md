# apkutils3 [![PyPI version](https://badge.fury.io/py/apkutils3.svg)](https://badge.fury.io/py/apkutils3) [![GitHub license](https://img.shields.io/github/license/Young-Lord/apkutils3.svg)](https://github.com/Young-Lord/apkutils3/blob/master/LICENSE)

A library that gets infos from APK.

Type hinting added for many functions.

Many getter functions are replaced by properties.

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

![apk parser example image](imgs/apk-parser.png)

## Reference

- apkutils\axml from [kin9-0rz/axmlparser](https://github.com/kin9-0rz/axmlparser) ![Project unmaintained](https://img.shields.io/badge/project-unmaintained-red.svg)
- apkutils\dex from [Storyyeller/enjarify](https://github.com/Storyyeller/enjarify) ![Project unmaintained](https://img.shields.io/badge/project-unmaintained-red.svg), license under Apache License 2.0.
- Original projects: [apkutils2](https://github.com/codeskyblue/apkutils2)  ![Project unmaintained](https://img.shields.io/badge/project-unmaintained-red.svg), [apkutils](https://github.com/kin9-0rz/apkutils), license under MIT License.
- [LibChecker](https://github.com/LibChecker/LibChecker) used for classes list generation, license under Apache License 2.0.
