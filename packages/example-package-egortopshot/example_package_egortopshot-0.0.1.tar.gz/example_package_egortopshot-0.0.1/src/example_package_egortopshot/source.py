import requests


class Source:
    def __init__(self, url):
        self.url = url

    def download(self):
        return requests.get(self.url)
