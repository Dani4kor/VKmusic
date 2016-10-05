#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re
import requests

from json import loads, dumps
from urllib import urlopen
from time import sleep

__author__ = 'ddani'

# only for python 2.7
reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = ''  # access token VK
USER_ID = ''  # user VK id
COUNT = 0  # 0 is max count of songs(5000)

audio_request = "https://api.vkontakte.ru/method/" \
                "audio.get?uid=" + USER_ID + \
                "&access_token=" + TOKEN + \
                "&count=" + str(COUNT)

audio = loads(requests.get(audio_request).text)

# debug api request
# print dumps(audio['response'] , indent=4, separators=(',', ': '))

path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "VKmusic")
if not os.path.exists(path):
    os.makedirs(path)
song_count, error_count = 0, 0
for i in audio['response']:
    song_count += 1
    if len(i['title']) >= 64:
        title = i['title'][0:len(i['title']) / 2]

    artist_title = "{}-{}.mp3".format(i['artist'], i['title'])
    # remove less symbols
    for match in re.findall('[?/\\!@#$%^&*+":;]', artist_title):
        artist_title = artist_title.replace(match, "")
    filename = os.path.join(path, artist_title).decode('utf-8')

    try:
        if not os.path.exists(filename):
            song = urlopen(i['url']).read()
            with open(filename, 'wb') as f:
                f.write(song)
                f.close()
                sleep(0.5)
        else:
            print"Song " + artist_title + " already exists"
            sleep(0.05)
    except IOError as e:
        print "IO ERROR [" + str(e.errno) + "] with " + artist_title + " try another type OR version song!\n"
        error_count += 1

print '\nDownloaded ' + str(song_count) + " | Available " + \
      str(loads(requests.get("https://api.vkontakte.ru/method/" + \
                             "audio.getCount?owner_id=" + USER_ID + \
                             "&access_token=" + TOKEN).text)['response']) + " | " + "Errors " + str(error_count)
print '\nSome songs can be closed by owners and are`t available through the API, but available on WEB/official' + \
      ' applications - VK support quote\n'
