from base_page1 import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SignUpPage(BasePage):

    SIGN_UP_LINK = (By.LINK_TEXT, "Sign up.")
    LOGIN_BUTTON = (By.XPATH, "//*[text()='Log In.']")
    PERSONAL_SELECT = (By.XPATH, "(//input[@type='radio'])[2]")
    CONTINUE_BUTTON = (By.XPATH, "//span[contains(.,'CONTINUE')]")
    FIRST_NAME = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    LAST_NAME = (By.XPATH, "//input[@type='text']")
    EMAIL_INSERT = (By.XPATH, "//input[@type='text']")
    EMAIL_MESSAGE_ERROR = (By.XPATH, "//p[text()='Please enter a valid email address.']")


    def click_sign_up_link(self):
        self.wait_and_click_elem(*self.SIGN_UP_LINK)

    def verify_url_signup(self):
        self.url_check("https://jules.app/sign-up")

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_url_sign_in(self):
        self.url_check("https://jules.app/sign-in")

    def select_personal(self):
        self.driver.find_element(*self.PERSONAL_SELECT).click()

    def click_continue_button(self):
        self.wait_and_click_elem(*self.CONTINUE_BUTTON)

    def set_first_name(self, firstname):
        self.driver.find_element(*self.FIRST_NAME).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*self.LAST_NAME).send_keys(lastname)

    def set_email(self,email):
        self.driver.find_element(*self.EMAIL_INSERT).send_keys(email)

    def verify_email_error_msg(self, expected_msg):
        try:
            actual_msg = self.driver.find_element(*self.EMAIL_MESSAGE_ERROR).text
        except NoSuchElementException:
            actual_msg = "None"
        assert actual_msg == expected_msg, f'Error! The message is not diplayed or incorrect, expected {expected_msg}, actual {actual_msg}'


    def clear_email_input(self):
        self.driver.find_element(*self.EMAIL_INSERT).click()
        self.driver.find_element(*self.EMAIL_INSERT).send_keys(Keys.CONTROL + "0" + Keys.DELETE)
