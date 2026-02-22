from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InformationPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_OUTPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CANCEL_BTN =(By.CLASS_NAME, "cart_cancel_link")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self, name=None, surname=None, zip=None):
        if name:
            self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(name)
        if surname:
            self.driver.find_element(*self.LAST_NAME_OUTPUT).send_keys(surname)
        if zip:
            self.driver.find_element(*self.ZIP_INPUT).send_keys(zip)
        self.driver.find_element(*self.CONTINUE_BTN).click()


    def click_cancel(self):
        self.driver.find_element(*self.CANCEL_BTN).click()


    def get_error_message(self):
        return self.wait.until(EC.presence_of_element_located(self.ERROR_MSG)).text