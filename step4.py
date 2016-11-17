import json
import requests
import yaml
import urllib2
from urllib2 import Request

token = {'token': 'dfd02630f543502ffb464929a71eafce'}

getCollection = requests.post('http://challenge.code2040.org/api/prefix', token)

d = yaml.load(getCollection.text)

withoutPrefix = []

print type(d)

for word in d['array']:
	if word.startswith(d['prefix']) == False:
		withoutPrefix.append(word)

print(withoutPrefix)

sendTo2040 = {'token': 'dfd02630f543502ffb464929a71eafce', 'array': withoutPrefix}
URL = 'http://challenge.code2040.org/api/prefix/validate'



request = Request(URL, sendTo2040)

request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(sendTo2040))

