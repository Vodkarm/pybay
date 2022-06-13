import requests

API_UPLOAD_URL = "https://api.bayfiles.com/upload"


class File:
    def __init__(self, file_path: str):
        """
        file_path: the file path to take care of
        """
        self.__file_path = file_path

    @property
    def file_path(self):
        return self.__file_path

    def upload(self, param: int):
        """
        Uploads the file to bayfiles.com
        """
        files = dict(file=open(self.file_path, "rb"))
        request = requests.post(API_UPLOAD_URL, files=files, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response = request.json()
        data = None

        if response["status"] == False:
            return "Your file is too large. Max size is 5GB !"
        data = response["data"]["file"]
        if param == 1:
            return data["metadata"]["id"]
        elif param == 2:
            return data["url"]["short"]
        return None
