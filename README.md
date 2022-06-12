# 🥳 PyBay

Hi! Welcome to the github of my first python package. Thanks you, and contributions are welcome.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000) ![Forks](https://img.shields.io/github/forks/vodkarm/pybay?style=social) ![Doc](https://img.shields.io/badge/Documentaion-yes-blue) ![Maintened](https://img.shields.io/badge/maintened%3F-yes-blue) ![GitHub Repo stars](https://img.shields.io/github/stars/vodkarm/pybay?style=social) [![Downloads](https://static.pepy.tech/personalized-badge/pybay?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/pybay)


# ❓ What is it ?
PyBay is a package that allow you to use bayfiles.com easily in python.

# 🌐 Is it open-source ?
Yes it is, but under MIT License

# 🕛 First time with PyBay
```bash
python3 -m pip install pybay
```
```py
from pybay import File
```
## 🌹 Uploading files
```py
from pybay import File

my_file = File("path/of/my/file.txt")
# You can use 1 or 2 as a response parameter (more below...)
my_file_url = my_file.upload(1)
print(my_file_url)
```

_**File.upload()**_ takes 1 argument, the response format :
- ``1`` : file id,
- ``2`` : file url.

Response format examples :
```bash
n7nad3p9yf # flag set to 1
https://bayfiles.com/n7nad3p9yf # flag set to 2
```

## 📛 Errors that you can get
***If your file is too large (more than 5GB), PyBay will respond:***
```
Your file is too large. Max size is 5GB !
```
## 💻 Fetch file info using PyBay
PyBay allow you to get informations about any files using his **bayfiles id**.
```py
from pybay import File, Info

my_file = File("myfile.txt")
my_file_id = my_file.upload(1)
my_file = Info(my_file_id)

print("Long file URL: " + my_file.long)
print("Short file URL: " + my_file.short)
print("File's Name: " + my_file.name)
print("File's Size: " + str(my_file.size.bytes))
```

## 📛 Errors that you can get
***If your file id is not found by PyBay, you will get this error:***
```
Invalid file ID was provided !
```
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
