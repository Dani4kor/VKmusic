# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

APPID = '5637720'
LOGIN = ''
PASSWORD = ''

driver = webdriver.Chrome()
driver.get("http://api.vkontakte.ru/oauth/authorize?"
           "client_id=5637720&scope=audio,offline"
           "&redirect_uri=https://oauth.vk.com/blank.html"
           "&display=page&response_type=token")

login_input = driver.find_element_by_name("email")
password_input = driver.find_element_by_name("pass")
login_input.send_keys(LOGIN)
password_input.send_keys(PASSWORD)

submit = driver.find_element_by_id("install_allow")
submit.click()

try:
    driver.implicitly_wait(2)
    submit = driver.find_element_by_id("install_allow")
    submit.click()
except NoSuchElementException:
    print "TOKEN has already been received"
finally:
    urllist = (driver.current_url.split("#"))[1].split("&")
    access_token, expires_in, user_id = (urllist[0].split("="))[1], \
                                        (urllist[1].split("="))[1], \
                                        (urllist[2].split("="))[1]

    print driver.current_url
    print user_id, access_token, expires_in

    driver.close()
