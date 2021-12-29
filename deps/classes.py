import requests
class url:
    def __init__(self, url: str):
        self.url = url
        self.rq = requests.get(url)
        self.content = self.rq.content