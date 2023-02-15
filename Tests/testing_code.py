import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException



class TEST(unittest.TestCase):
    EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BUTTON = (By.XPATH, "//*[text()='Log in']")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//*[text()='Please enter your password!']")
    BUTTON_DISABLED = (By.XPATH, "//button[@data-test-id='login-button']")
    SIGN_UP_LINK = (By.LINK_TEXT, "Sign up.")
    PERSONAL_SELECT = (By.XPATH, "(//input[@type='radio'])[2]")
    CONTINUE_BUTTON = (By.XPATH, "//*[text()='CONTINUE']")
    CONTINUE_BUTTON2 = (By.XPATH, '//button[@data-test-id="first-name-continue-btn"]')
    CONTINUE_BUTTON3 = (By.XPATH, '//span[contains(.,"CONTINUE")]')
    FIRST_NAME = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    LAST_NAME = (By.XPATH, "//input[@type='text']")
    EMAIL_INSERT = (By.XPATH, "//*[@class='MuiInputBase-input MuiFilledInput-input']")
    EMAIL_MESSAGE_ERROR = (By.XPATH, "//p[text()='Please enter a valid email address.']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get("https://jules.app/sign-in")

    def tearDown(self):
        self.driver.quit()


    # test 1
    def test_01_email(self):
        self.driver.find_element(*self.EMAIL_INSERT).send_keys("test1@microsoft.com")
        sleep(1)

    def test_02_verify_email_error_msg(self):
        self.test_01_email()
        expected_msg = "Please enter your password!"
        try:
            actual_msg = self.driver.find_element(*self.PASSWORD_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_msg = "None"
        assert actual_msg != expected_msg, f"Error! The message is not displayed{actual_msg}, and expected{expected_msg}"
        sleep(3)

    def test_03_verify_login_button_disabled(self):
        self.test_01_email()
        elem_login_button = self.driver.find_element(*self.BUTTON_DISABLED)
        self.assertFalse(elem_login_button.is_enabled(), "Button LOGIN it is not disabled")
        sleep(3)


    # test2
    def test_04_click_sign_up_link(self):
        sleep(5)
        self.driver.find_element(*self.SIGN_UP_LINK).click()
        sleep(5)

    def test_05_url_check_sign_up(self, expected_url= "https://jules.app/sign-up"):
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "The url is incorrect")

    def test_06_click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def test_07_url_check_sign_in(self, expected_url= "https://jules.app/sign-in"):
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url, "The url is incorrect")



    def test_test3(self):
        self.driver.find_element(*self.SIGN_UP_LINK).click()
        sleep(1)
        self.driver.find_element(*self.PERSONAL_SELECT).click()
        sleep(1)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(1)
        self.driver.find_element(*self.FIRST_NAME).send_keys("Andrei")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(1)
        self.driver.find_element(*self.LAST_NAME).send_keys("Vlad")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(1)
        self.driver.find_element(*self.EMAIL_INSERT).send_keys("test2@microsoft.com")
        sleep(2)
        expected_message = "None"
        try:
            actual_message = self.driver.find_element(*self.EMAIL_MESSAGE_ERROR).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, f'Error! The message is incorrect, expected {expected_message}, actual {actual_message}'



    # def test_set_password(self):
    #     self.test_email()
    #     self.driver.find_element(*self.PASSWORD).send_keys("test1234")
    #     sleep(3)

    # def test_click_login_button(self):
    #     self.driver.find_element(*self.LOGIN_BUTTON).click()
    #     sleep(3)
