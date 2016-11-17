import json
import requests
import yaml
import datetime
import urllib2
from urllib2 import Request

token = {'token': 'dfd02630f543502ffb464929a71eafce'}

getDateAndTime = requests.post('http://challenge.code2040.org/api/dating', token)

print getDateAndTime.text

d = yaml.load(getDateAndTime.text)


timeNot = d['datestamp']
seconds = d['interval']


# Get All substrings that have the dates, convert them into int, put them in time class
time = datetime.datetime(int(timeNot[0:4]), int(timeNot[5:7]), int(timeNot[8:10]), int(timeNot[11:13]), int(timeNot[14:16]), int(timeNot[17:19]))

delta = datetime.timedelta(seconds = seconds)

time = time + delta

isoTime = time.isoformat() + "Z"


sendTo2040 = {'token': 'dfd02630f543502ffb464929a71eafce', 'datestamp': isoTime}
URL = 'http://challenge.code2040.org/api/dating/validate'



request = Request(URL, sendTo2040)

request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(sendTo2040))