# Apk Analyzer

A python script to analyze apk files. 

dangerous_permission.json was prepared from [Manifest.permission](https://developer.android.com/reference/android/Manifest.permission)

*New modules will be added*

## How it works ?
The tools uses [Androguard](https://github.com/androguard/androguard) library.
- Get permissions with get_permission() function.
- Print them to the screen.

## Installation

> pip install -U androguard

## Usage

> python3 apk_analyzer.py [APK] 

## Example

> python3 apk_analyzer.py Test.apk

<img src="/pics/apk_analyzer.png"
     style="float: left; margin-right: 10px;" />