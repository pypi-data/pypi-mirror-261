import json
import sys
from zipfile import ZipFile
from pathlib import Path
import argparse

CHIP_FAMILIES = ["ESP32", "ESP8266"]
OUTPUT_FILE = "firmware.zip"
BUILD_BASE_FOLDER = ".pio/build"
IDEDATA_FILENAME = "idedata.json"
FIRMWARE_FILENAME = "firmware.bin"


def prompt(message):
    sys.stdout.write(message + "\n")


def error(message):
    sys.stderr.write(message + "\n")


def line():
    prompt("-" * 80)


def fatal(message):
    error(message)
    exit(1)


def scan_builds(base_folder: str, idedata_filename: str):
    builds = []
    build_base = Path(base_folder)
    if build_base.exists() and build_base.is_dir():
        for path in build_base.glob("**/" + idedata_filename):
            builds.append({
                "path": str(path.parent),
                "board": str(path.resolve().parent.stem)
            })
    return builds


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fw-name", help="Firmware name to use", default=None)
    parser.add_argument("--fw-version", help="Firmware version to use", default=None)
    parser.add_argument("--build-base", help="PlatformIO build base folder", default=BUILD_BASE_FOLDER)
    parser.add_argument("--idedata", help="PlatformIO offset map file", default=IDEDATA_FILENAME)
    parser.add_argument("--firmware", help="PlatformIO firmware file", default=FIRMWARE_FILENAME)
    parser.add_argument("--output", help="Output file", default=OUTPUT_FILE)
    return parser.parse_args()


def select_build(builds: list) -> int:
    while True:
        prompt("Multiple builds found. Please select which one to use, or 0 to exit:")
        for index, build in enumerate(builds):
            prompt(f" [{index + 1}] {build['board']} ({build['path']})")

        try:
            num = int(sys.stdin.readline())
            if num == 0:
                return -1

            if 0 < num <= len(builds):
                return num - 1
        except ValueError:
            error("Invalid choice.")


def select_family(families: list) -> int:
    while True:
        prompt("Chip Family, or 0 to exit:")
        for index, family in enumerate(families):
            prompt(f" [{index + 1}] {family}")
        try:
            num = int(sys.stdin.readline())
            if num == 0:
                return -1

            if 0 < num <= len(families):
                return num - 1
        except ValueError:
            error("Invalid choice.")


def get_firmware_name(fw_name: str):
    while not fw_name:
        line()
        prompt("Enter firmware name to use: ")
        fw_name = str(sys.stdin.readline())
    return fw_name


def get_firmware_version(fw_version: str):
    while not fw_version:
        line()
        prompt("Enter firmware version to use: ")
        fw_version = str(sys.stdin.readline())
    return fw_version


def get_firmware_files(idedata_file: Path, build_path: str, firmware_file: str) -> list:
    firmware_files = []
    try:
        with open(idedata_file) as f:
            idedata = json.load(f)

            firmware_files.append({
                "file": f"{build_path}/{firmware_file}",
                "offset": idedata["extra"]["application_offset"]
            })
            for part in idedata["extra"]["flash_images"]:
                firmware_files.append({
                    "file": part["path"],
                    "offset": part["offset"]
                })
        return firmware_files

    except Exception as e:
        fatal(f"Fatal Error: \n {e}")


def main():
    args = parse_args()
    builds = scan_builds(args.build_base, args.idedata)
    if len(builds) == 0:
        fatal("No build folders have been found. Please build and upload the project first.")

    build = None
    if len(builds) > 1:
        idx = select_build(builds)
        if idx == -1:
            fatal("Aborted by user")
        build = builds[idx]
    else:
        build = builds[0]
        line()
        prompt(f"Using build: {build['board']} ({build['path']})")

    firmware_name = get_firmware_name(args.fw_name)
    version = get_firmware_version(args.fw_version)
    chip_family = select_family(CHIP_FAMILIES)
    if chip_family == -1:
        fatal("Aborted by user")

    idedata = Path(f"{build['path']}/{args.idedata}")
    if not idedata.exists() or not idedata.is_file():
        fatal("File {idedata} not found")
    firmware_files = get_firmware_files(idedata, build["path"], args.firmware)

    try:
        line()
        prompt("Generating zip file...")
        parts = []
        with ZipFile(args.output, "w") as zip_object:
            for record in firmware_files:
                prompt(f"Adding: {Path(record['file']).absolute()}... ")
                zip_object.write(record["file"], arcname=record["offset"] + "_" + record["file"].split("/")[-1])
                parts.append({
                    "path": record["offset"] + "_" + record["file"].split("/")[-1],
                    "offset": str(int(record["offset"], 16)),
                })

            manifest = {
                "name": firmware_name,
                "version": version,
                "builds": [
                    {
                        "chipFamily": chip_family,
                        "parts": parts
                    }
                ]
            }
            zip_object.writestr("manifest.json", json.dumps(manifest, indent=2))

        prompt("Done!")
        exit(0)

    except Exception as e:
        fatal(f"Fatal Error: \n {e}")
