import requests

API_FILE_URL = "https://api.bayfiles.com/v2/file/{}/info"


class Size:
    """
    Represents the different ways to get a size of a file
    from bayfiles.com :
    - bytes,
    - readable.
    """

    def __init__(self, metadata: dict):
        """
        metadata: the metadata fetched from a file id
        """
        self.__metadata = metadata
        if not "size" in self.__metadata:
            raise "Invalid metadata was provided !"
        self.__bytes = self.__metadata["size"]["bytes"]
        self.__readable = self.__metadata["size"]["readable"]

    @property
    def bytes(self):
        return self.__bytes

    @property
    def readable(self):
        return self.__readable


class Info:
    def __init__(self, file_id: str):
        """
        file_id: the file id from bayfiles.com which will be fetched
        """
        self.__id = file_id
        self.__data = requests.get(API_FILE_URL.format(self.id)).json()
        if not self.__data["status"]:
            raise "Invalid file ID was provided !"
        self.__data = self.__data["data"]["file"]
        self.__name = self.__data["metadata"]["name"]
        self.__size = Size(self.__data["metadata"])
        self.__short = self.__data["url"]["short"]
        self.__long = self.__data["url"]["full"]

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def short(self):
        return self.__short

    @property
    def long(self):
        return self.__long
