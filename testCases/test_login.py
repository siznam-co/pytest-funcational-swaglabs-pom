from pageObjects.LoginPage import LoginPage
from utilities.conftest import *
import allure


class Test_Login:

    @allure.description("Verify that the user is able to Login with standard user")
    def test_verify_login_standard_user(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.success_login(get_config("CREDS", "standard_user"),get_config("CREDS", "password"))

    @allure.description("Verify that the user is able to Login with locked user")
    def test_verify_login_locked_user(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.glitch_login(get_config("CREDS", "locked_user"),get_config("CREDS", "password"))

    @allure.description("Verify that the user is able to Login with problem user")
    def test_verify_login_problem_user(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.success_login(get_config("CREDS", "problem_user"),get_config("CREDS", "password"))

    @allure.description("Verify that the user is NOT able to Login with performance glitch user")
    def test_verify_login_problem_glitch_user(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.success_login(get_config("CREDS", "performance_glitch_user"),get_config("CREDS", "password"))


