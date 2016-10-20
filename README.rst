VKmusic
=======

Simple python music downloader from VK.com

**author** = “ddani”

Setup:
------

-  Python2.7

::

    pip install -r requirements.txt

Dependencies: \* `selenium`_ -> need only for oauthselenium \*
`requests`_

Usage:
------

-  Create VK `standalone application`_
-  Get ``ACCESS TOKEN`` for audio method OR you can use
   ``oauthselenium.py`` -> write your Login/Phone, Password and APPID in
   appropriate variables and script will print ``ACCESS TOKEN``, user
   ID, expire TOKEN

::

    Default Selenium webdrive - Chrome, you can change it, BEWARE bugs with Firefox v48!

`Chromihmdriver`_ also in repo

-  use ``ACCESS TOKEN`` and userid in ``vkmusic.py``

-  vkmusic.py will create VKmusic folder in directory, and start
   Download all music(start from top) that you have in your VK acc
-  Script also Overwrite same music and except IO errors -> info about
   ERROR and Songs you will see in Console \`\`\` IO ERROR [2] with
   GanGuBaS ft. Bizaro ft. Christina Luck - !@#$%^&\*()0-9a-zA-z

Song Mavis Staples-Will The Circle Be Unbroken.mp3 already exists Song
Mavis Staples-Step Into The Light.mp3 already exists \`\`\`

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