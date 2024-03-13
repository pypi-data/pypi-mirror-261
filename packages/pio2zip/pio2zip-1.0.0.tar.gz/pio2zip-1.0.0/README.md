PIO2ZIP 
=======
[![pypi](https://img.shields.io/pypi/v/pio2zip.svg)](https://pypi.org/project/pio2zip/)
[![license](https://img.shields.io/pypi/l/pio2zip.svg)](https://github.com/blackshieldpt/pio2zip/blob/master/LICENSE)


pio2zip is a cli tool to generate a zipfile from PlatformIO ESP32/ESP8266 generated binaries to aid the flashing of
firmwares using [whysoserial.cc](https://whysoserial.cc). 

## Installation

Install via pip package:

```shell
$ pip install pio2zip
```

## Usage

```python
usage: pio2zip [-h] [--fw-name FW_NAME] [--fw-version FW_VERSION] [--build-base BUILD_BASE] [--idedata IDEDATA] [--firmware FIRMWARE] [--output OUTPUT]

options:
  -h, --help            show this help message and exit
  --fw-name FW_NAME     Firmware name to use
  --fw-version FW_VERSION
                        Firmware version to use
  --build-base BUILD_BASE
                        PlatformIO build base folder
  --idedata IDEDATA     PlatformIO offset map file
  --firmware FIRMWARE   PlatformIO firmware file
  --output OUTPUT       Output file
```