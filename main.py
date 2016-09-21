# -*- coding: utf-8 -*-

import vk, sys, json

# only for python 2.7
reload(sys)
sys.setdefaultencoding("utf-8")

# ACCESS TOKEN
TOKEN = ''


session = vk.Session(access_token=TOKEN)
api = vk.API(session)

print json.dumps(api.users.get(user_ids=1), indent=4, separators=(',', ': '))


