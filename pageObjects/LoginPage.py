import time
from selenium import webdriver
import allure
import pdb
from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage

class LoginPage(BasePage):
    login_locators = {
        "email_label": (By.ID, "user-name"),
        "password_label": (By.ID, "password"),
        "login_button": (By.ID, 'login-button'),
        "page_title": (By.XPATH, '//*[@id="header_container"]/div[2]/span'),
        "error_button": (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    }

    def success_login(self, email, password):
        self.send_text_to_element(self.find_element(self.login_locators["email_label"]), email)
        self.send_text_to_element(self.find_element(self.login_locators["password_label"]),password)
        self.click_element(self.login_locators["login_button"])

        success_assert = self.get_element_text(self.find_element(self.login_locators["page_title"]))
        if success_assert == "PRODUCTS":
            logged_in_user = self.driver.get_cookie('session-username')['value']
            assert email == logged_in_user, email + " = Sign In Failed!"
        else:
            assert False, email + " = Sign In Failed!"

    def glitch_login(self, email, password):
        self.send_text_to_element(self.find_element(self.login_locators["email_label"]), email)
        self.send_text_to_element(self.find_element(self.login_locators["password_label"]), password)
        self.click_element(self.login_locators["login_button"])
        fail_assert = self.get_element_text(self.find_element(self.login_locators["error_button"]))
        if fail_assert == "Epic sadface: Sorry, this user has been locked out.":
            assert True, email + " = Sign In Failed!"
        else:
            assert False, email + " = Sign In Failed!"
