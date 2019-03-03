# Automatic Saving Script

## What this script is

Automatically saves your work by auto-typing "CTRL-S" every 5 minutes.
Made this to fool around with the SendKeys library. Works exactly as advertised.

## Why I would want this

You probably don't. This is simply a personal proof-of-concept that I
almost refrained from uploading in the first place. It's honestly
probably not worth your time if you are at all familiar with python.

If you aren't, however, feel free to download and use.

## 3 ways to use

Running the python script is the easiest (and safest) way to use the program,
but that obviously may not be convenient for less tech savvy people. Because
of this, there are 3 ways to run the autosave script:

### Easy, Simple Route (Windows Only)

* Download the .exe in the `dist` folder. It should work, for 64-bit systems!
  1. Please tell me if it doesn't.

### Medium, Python route (All Platforms)

Install the following:

* python
* pip (to install SendKeys)
* SendKeys python library

then, open a terminal/cmd/powershell window and execute:

`python autosave.py`

The script will begin and execute from the terminal!

### Hard, DIY route

If you'd like you can also compile my script into an executable!
That's how I made the `.exe` for Windows users. Simply install:

* python
* pip (to install SendKeys)
* SendKeys python library
* pyinstaller python library

Then, execute:

`pyinstaller --onefile autosave.py`

You've now created your own executable for your platform of choice!
