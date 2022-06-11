import requests

class File():
  global base
  base = "https://api.bayfiles.com/"
  # filePath parameter represent the file path that will be uploaded in bayfiles.com
  def Upload(filePath, param):
    file = {
      'file': (open(filePath, "rb")),
    }
    r = requests.post(base + "upload", files=file)
    if r.json()["status"] == False:
      return "Your file is too large. Max size is 5GB"
    elif param == 1:
      return r.json()["data"]["file"]["metadata"]["id"]
    elif param == 2:
      return r.json()["data"]["file"]["url"]["short"]
class Info():
    # id parameter represent the file id (that's hosted on bayfile) which will be used to get informations
  def Long(id):
    r = requests.get(base + "v2/file/" + id + "/info")
    if r.json()["status"] == False:
      return "This file doesn't exist, sorry."
    else:
      return r.json()["data"]["file"]["url"]["full"]
  def Short(id):
    r = requests.get(base + "v2/file/" + id + "/info")
    if r.json()["status"] == False:
      return "This file doesn't exist, sorry."
    else:
      return r.json()["data"]["file"]["url"]["short"]
  def Name(id):
    r = requests.get(base + "v2/file/" + id + "/info")
    if r.json()["status"] == False:
      return "This file doesn't exist, sorry."
    else:
      return r.json()["data"]["file"]["metadata"]["name"]
  def Size(id, param):
    r = requests.get(base + "v2/file/" + id + "/info")
    if r.json()["status"] == False:
      return "This file doesn't exist, sorry."
    elif param == 1:
      return r.json()["data"]["file"]["metadata"]["size"]["bytes"]
    elif param == 2:
      return r.json()["data"]["file"]["metadata"]["size"]["readable"]
