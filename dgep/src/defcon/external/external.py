import requests

class ExternalURI:

    def call(self, uri, content={}):
        if content:
            response = requests.post(uri, data=content)
        else:
            response = requests.post(uri)

    def get(self, uri):
        response = requests.get(uri)

        if response.status_code == 200:
            return response.text
        else:
            return ""

    def test(self, uri, content={}):
        if content:
            response = requests.post(uri, data=content)
        else:
            response = requests.post(uri)

        if response.status_code == 200:
            #should evaluate to True or False
            if response.text in ("True","true","1"):
                return True

        return False
