from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BTN = (By.CLASS_NAME, "cart_button")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[@data-test='continue-shopping']")
    CHECKOUT_BTN = (By.XPATH, "//button[@data-test='checkout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def get_item_count(self):
        n_items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM))
        return len(n_items)

    def get_cart_badge_count(self):
        return self.wait.until(EC.presence_of_element_located(self.CART_ICON)).find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def remove_first_item(self):
        remove_button = self.wait.until(EC.visibility_of_all_elements_located(self.REMOVE_BTN))
        remove_button[0].click()

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def click_continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BTN)).click()
