VKmusic
=======

Simple python music downloader from VK.com

**author** = “ddani”

Setup:
------

-  Python2.7

::

    pip install -r requirements.txt

Dependencies: \* `selenium`_ -> need only for selenium_gettoken.py \*
`requests`_

Usage:
------

-  Create VK `standalone application`_
-  Get ``ACCESS TOKEN`` for audio method OR you can use
   ``selenium_gettoken.py`` requires selenium depend
::

    >>> from selenium_gettoken import *
    >>> info = Gettoken(appid, login, password)
    >>> token = info.token()
    {'access_token':'XXXXXXX', 'expires_in':'XXXX', 'user_id':'XXXXXX'}

::

    Default Selenium webdrive - Chrome, you can change it, BEWARE bugs with Firefox v48!

`Chromihmdriver`_ also in repo

-  use ``ACCESS TOKEN`` and userid in ``vkmusic.py``

::

    >>> import vkmusic
    >>> vk.music.downloadmusic(ACCESS TOKEN, USER ID, COUNT=0)
    >>> token = info.token()
    {'access_token':'XXXXXXX', 'expires_in':'XXXX', 'user_id':'XXXXXX'}
Fix & Tips
----------

-  Main problems of IOerrors are bad information in artist/title name,
   try to add another version of song
-  Socket problems - change IDE or Console and rerun vkmusic.py

VK API
------

-  Some of songs has Copyright protection, what means API didn\`t answer
   you full list of songs, but you still can find another version of
   song - add it to audio and try again!.

.. _selenium: https://github.com/SeleniumHQ/selenium
.. _requests: https://github.com/kennethreitz/requests
.. _standalone application: https://vk.com/editapp?act=create
.. _Chromihmdriver: https://sites.google.com/a/chromium.org/chromedriver/