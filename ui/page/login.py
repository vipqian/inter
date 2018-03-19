# coding=utf-8

from lianxi_ui_interface.common.find_element import FindElement, browser
login_url = "https://mydev.100szy.com/#/login"
import time


class LoginPage(FindElement):
    login_loc = ('css', '#login_wrap > div.loginTitle > span:nth-child(1)')
    phone_login_loc = ('css', '#login_wrap > div.loginTitle > span:nth-child(2)')
    name_loc = ('css', '#login_wrap > div:nth-child(3) > div:nth-child(1) > input[type="text"]')
    password_loc = ('css', '#login_wrap > div:nth-child(3) > div:nth-child(2) > input[type="password"]')
    remember_loc = ('css', '#login_wrap > div.loginOperator > img:nth-child(1)')
    forgot_password_loc = ('css', '#login_wrap > div.loginOperator > span:nth-child(4)')
    login_button_loc = ('css', '#login_wrap > div:nth-child(6)')
    register_loc = ('css', '#login_wrap > div.sanfang > span:nth-child(5)')

    def click_phone_login(self):
        self.click(self.phone_login_loc)

    def click_login(self):
        self.click(self.login_loc)

    def input_name(self, username):
        self.send_keys(self.name_loc, username)

    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    def click_login_button(self):
        self.click(self.login_button_loc)

    def click_remember(self):
        self.click(self.remember_loc)

    def click_forgot_password(self):
        self.click(self.forgot_password_loc)

    def click_register(self):
        self.click(self.register_loc)

if __name__ == '__main__':
    driver = browser()
    browser = LoginPage(driver)
    browser.open_url(login_url)
    # browser.input_name('13944096337')
    # browser.input_password('114547')
    # browser.click_login_button()
    # browser.click_remember()
    # locator = ('css', '#reg_wrap > div.loginTitle > span:nth-child(1)')

    browser.click_register()
    locator = ('css', '#reg_wrap > div.loginTitle > span:nth-child(1)')
    text = browser.get_text(locator)
    print(text)
