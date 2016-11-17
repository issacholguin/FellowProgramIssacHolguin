import json
import requests

token = {'token': 'dfd02630f543502ffb464929a71eafce'}

getString = requests.post('http://challenge.code2040.org/api/reverse', token)

print (getString.text)

reversedString = getString.text[::-1];

print(reversedString)

sendTo2040 = {'token': 'dfd02630f543502ffb464929a71eafce', 'string': reversedString}

URL = 'http://challenge.code2040.org/api/reverse/validate'

request = requests.post(URL, sendTo2040)

print(request.text)
print(request.status_code)