# 🥳 PyBay

Hi! Welcome to the github of my first python package.
 Thanks you, and contributions are welcome.
 
 <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" /> <img alt="Forks" src="https://img.shields.io/github/forks/vodkarm/pybay?style=social"> <img alt="doc" src="https://img.shields.io/badge/Documentaion-yes-blue"> <img alt="maintened" src="https://img.shields.io/badge/maintened%3F-yes-blue"> ![GitHub Repo stars](https://img.shields.io/github/stars/vodkarm/pybay?style=social) [![Downloads](https://pepy.tech/badge/pybay)](https://pepy.tech/project/pybay)


 # ❓ What is it ?
PyBay is a package that allow you to use bayfiles.com easily in python.
# 🌐 Is it open-source ?
Yes it is, but under MIT License 
# 🕛 First time with PyBay
```
pip install pybay
```
```py
from pybay import File
```
## 🌹 Uploading files
```py
from pybay import File
print(File.Upload("path/of/my/file.txt", 1) # You can use 1 or 2 as a response parameter (more below...)
```
_**File.Upload()**_ need 2 arguments 
 - **FilePath**
 - **Response type** (_1 or 2_)
For _Response type_, **1** will return file id and **2** will return file url<br>
_**1** response exemple_:
```
n7nad3p9yf
```
_**2** response exemple_:
```
https://bayfiles.com/n7nad3p9yf
```
## 📛 Errors that you can get
***If your file is too large (more than 5GB), PyBay will respond:***
```
Your file is too large. Max size is 5GB
```
## 💻 Get file infos using PyBay
PyBay allow you to get informations about any files using his **bayfiles id**.
```py
from pybay import File, Info
print("Long file URL: " + Info.Long(File.Upload("myfile.txt", 1))
print("Short file URL: " + Info.Short(File.Upload("myfile.txt", 1))
print("File's Name: " + Info.Name(File.Upload("myfile.txt", 1))
print("File's Size: " + Info.Size(File.Upload("myfile.txt", 1), 1) # In this situation, 2 can't work because it return the link and not the id.
```
***Info.Size*** need 2 arguments:
 - **FilePath**
 - **ResponseType**
For ResponseType, 1 will return file size in bytes and 2 will return file size as a readable text
**1** Response exemple:
```
[...]
File's Size: 8
```
**2** Response exemple:
```
[...]
File's Size: 8 B
```
## 📛 Errors that you can get
***If your file id is not found by PyBay, you will get this error:***
```
This file doesn't exist, sorry.
```
# ✨ Dependencies
**PyBay** has only 1 dependencies 🥳 !
It's only using **requests** !
## 👤 Author
👤 GitHub: [@**vodkarm**](https://github.com/vodkarm)
## 🤝 Contributing
Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/vodkarm/pybay/issues).
## ❤ Show your support
Give a ⭐️ if this project helped you!
## 🤔 Creator message
This package is my first, before I never created any packages.
It was did in only 30 minutes, I know this code is not perfect but It work.
Thanks for all <3
