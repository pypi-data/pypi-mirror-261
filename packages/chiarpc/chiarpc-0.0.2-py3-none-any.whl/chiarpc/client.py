import json
from urllib.parse import urljoin

import requests


class Client:
    def __init__(self, base_url, private_cert_file, private_key_file):
        self.base_url = base_url
        self.private_cert_file = private_cert_file
        self.private_key_file = private_key_file

    def call(self, endpoint, data=None):
        if data is None:
            data = {}
        headers = {'Content-Type': 'application/json'}
        url = urljoin(self.base_url, endpoint)
        cert = (self.private_cert_file, self.private_key_file)
        response = requests.post(url, data=json.dumps(data), headers=headers, cert=cert, verify=False)
        return response.json()
