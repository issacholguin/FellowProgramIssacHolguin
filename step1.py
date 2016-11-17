import json
import requests

URL = 'http://challenge.code2040.org/api/register'

data = {'token': 'dfd02630f543502ffb464929a71eafce', 'github': 'https://github.com/issacholguin/FellowProgramIssacHolguin'}

dumpdata = json.dumps(data)

request = requests.post(URL, data)

print(request.text)
print(request.status_code)