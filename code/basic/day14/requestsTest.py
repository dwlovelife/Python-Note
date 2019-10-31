from time import time
from threading import Thread
import requests

# 继承Thread类创建的自定义类


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1]
        resp = requests.get()
