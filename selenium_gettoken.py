#!/usr/bin/env python
# -- coding: utf-8 --


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Gettoken():
    def __init__(self, appid=5637720, login=str, password=str):
        self.appid = str(appid)
        self.login = login
        self.password = password
        self.driver = webdriver.Chrome()

        self.driver.get("http://api.vkontakte.ru/oauth/authorize?"
                        "client_id=5637720&scope=audio,offline"
                        "&redirect_uri=https://oauth.vk.com/blank.html"
                        "&display=page&response_type=token")

        login_input = self.driver.find_element_by_name("email")
        password_input = self.driver.find_element_by_name("pass")
        login_input.send_keys(self.login)
        password_input.send_keys(self.password)

        submit = self.driver.find_element_by_id("install_allow")
        submit.click()

        try:
            self.driver.implicitly_wait(2)
            submit = self.driver.find_element_by_id("install_allow")
            submit.click()
        except NoSuchElementException:
            print "TOKEN has already been received"
        finally:
            self.rtrtoen()
            self.driver.close()

    def rtrtoen(self):
        urllist = (self.driver.current_url.split("#"))[1].split("&")
        access_token, expires_in, user_id = (urllist[0].split("="))[1], \
            (urllist[1].split("="))[1], \
            (urllist[2].split("="))[1]
        return {'user_id': user_id, 'access_token': access_token, 'expires_in': expires_in}
