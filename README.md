VKmusic
-------



#**VK.com closed his public audio api on 16 dec 2016**

Simple python console music downloader from VK.com through VK API

Setup:
------

-   Python2.7

<!-- -->

    pip install -r requirements.txt

Dependencies:

-   \* [selenium] -&gt; need only for selenium\_gettoken.py \*
-   [requests]

Usage:
------

-   Create VK [standalone application]
-   Get `ACCESS TOKEN` for audio method OR you can use `selenium_gettoken.py` requires selenium depend

<!-- -->

    >>> from selenium_gettoken import *
    >>> info = Gettoken(appid, login, password)
    >>> token = info.token()
    {'access_token':'XXXXXXX', 'expires_in':'XXXX', 'user_id':'XXXXXX'}

    Default Selenium webdrive - Chrome, you can change it, BEWARE bugs with Firefox v48!

[Chromihmdriver] also in repo

-   use `ACCESS TOKEN` and userid in `vkmusic.py`

<!-- -->

    >>> import vkmusic
    >>> vk.music.downloadmusic(ACCESS TOKEN, USER ID, COUNT=0)
    >>> token = info.token()
    Song XXXX.mp3 Downloaded
    Song XXXX.mp3 already exists
    Downloaded XX | Available XX | Errors X

Fix & Tips
----------

-   Main problems of IOerrors are bad information in artist/title name, try to add another version of song
-   Socket problems - change IDE or Console and rerun vkmusic.py

VK API
------

-   Some of songs has Copyright protection, what means API didn\`t answer you full list of songs, but you still can find another version of song - add it to audio and try again!.

LICENSE
------
This project is licensed under the GPLv3 see the LICENSE file for details

  [selenium]: https://github.com/SeleniumHQ/selenium
  [requests]: https://github.com/kennethreitz/requests
  [standalone application]: https://vk.com/editapp?act=create
  [Chromihmdriver]: https://sites.google.com/a/chromium.org/chromedriver/
