# TH3D-Marlin2-EZBoard-cli-compiler

## 1.Config the firmware

Download the [TH3D-Unified-U2.R1 firmware](https://github.com/houseofbugs/TH3D-Unified-U2.R1) and edit the config files to match your machine config.

## 2.Install python

Download python from [Python homepage](https://www.python.org/downloads/) and install it. Remember to check the <code>Add Python 3.7 to PATH</code> option.  

![alt text](https://github.com/ChipTechno/TH3D-Marlin2-EZBoard-cli-compiler/blob/master//img/img-00.png "Python installer")

## 3.Install platformio core

Open <code>cmd</code> and type <code>pip install platformio</code> then press <button>ENTER</button>.  

![alt text](https://github.com/ChipTechno/TH3D-Marlin2-EZBoard-cli-compiler/blob/master//img/img-01.png "platformio installer")

## 4.Download compile script

Download the [compile-cli.py](https://raw.githubusercontent.com/ChipTechno/TH3D-Marlin2-EZBoard-cli-compiler/master/compile-cli.py) file and put it in the <code>TH3D-Unified-U2.R1</code> folder.

## 5.Run the compile script

Double click the <code>compile-cli.py</code> and wait for the compile to complete. The firmware file will be copy to <code>Bin</code> folder.
