import json
import os
import shutil
import sys

MARLIN_PATH = "Marlin/"
OUTPUT_DIR = "Bin/"
ENVI_NAME = "LPC1769"
AUTO_COMPILE_VERSION = "v0.1.0"
DEBUG = True

############################ FUNCTIONS ##################################
def debugMsg(msg):
    if DEBUG:
        print(msg)

#########################################################################

print("Marlin 2 firmware cli compiler " + AUTO_COMPILE_VERSION + "\n")

# make folder for output file
try:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except FileExistsError:
    # directory already exists
    pass

# Execute platformio build
os.system("platformio run -e "+ENVI_NAME)

# copy binary file to OUTPUT_DIR
print("\nCopy binary output file to " + OUTPUT_DIR + "firmware.bin")
shutil.copy(".pioenvs/"+ ENVI_NAME +"/firmware.bin", OUTPUT_DIR + "firmware.bin")
# cleanup
print("Cleanup platformio build folder...")
shutil.rmtree(".pioenvs")
shutil.rmtree(".piolib")
shutil.rmtree(".piolibdeps")
print("Done :3")
print("Press ENTER to exit.")
input()
sys.exit(0)
