import json
import requests
import yaml

token = {'token': 'dfd02630f543502ffb464929a71eafce'}

getString = requests.post('http://challenge.code2040.org/api/haystack', token)

# Converts string to Dictionary using yaml
d = yaml.load(getString.text)

# No loop needed!
index = d['haystack'].index(d['needle'])

# to check myself!
print(d)
print(index)

sendTo2040 = {'token': 'dfd02630f543502ffb464929a71eafce', 'needle': index}

URL = 'http://challenge.code2040.org/api/haystack/validate'

request = requests.post(URL, sendTo2040)

print(request.text)
print(request.status_code)