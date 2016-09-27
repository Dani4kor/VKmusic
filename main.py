# -*- coding: utf-8 -*-

import vk, sys, os, urllib, re
from time import sleep

# only for python 2.7
reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = ''
USER_ID = ''

session = vk.Session(access_token=TOKEN)
api = vk.API(session)
audio = api.audio.get(user_ids=USER_ID)

# debug api request
# print json.dumps(api.audio.get(user_ids=USER_ID), indent=4, separators=(',', ': '))  #

path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "VKmusic")
if not os.path.exists(path):
    os.makedirs(path)

for i in audio:
    if len(i['title']) >= 64:
        title = i['title'][0:len(i['title']) / 2]

    artist_title = "{}-{}.mp3".format(i['artist'], i['title'])
    # remove less symbols
    for match in re.findall('[?/\\!@#$%^&*+":;]', artist_title):
        artist_title = artist_title.replace(match, "")
    filename = os.path.join(path, artist_title)

    try:
        if not os.path.exists(filename):
            song = urllib.urlopen(i['url']).read()
            with open(filename, 'wb') as file:
                file.write(song)
                file.close()
                sleep(0.5)
        else:
            print"Song " + artist_title + " already exists"
            sleep(0.05)
    except IOError as e:
        print "IO ERROR [" + str(e.errno) + "] with " + artist_title + " try another type OR version song!\n"






