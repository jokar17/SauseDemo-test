from selenium.webdriver.common.by import By

class CartPage:

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BTN = (By.CLASS_NAME, "cart_button")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[@data-test='continue-shopping']")
    CHECKOUT_BTN = (By.XPATH, "//button[@data-test='checkout']")

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        n_items = self.driver.find_elements(*self.CART_ITEM)
        return len(n_items)

    def get_cart_badge_count(self):
        return self.driver.find_element(*self.CART_ICON).find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def remove_first_item(self):
        remove_button = self.driver.find_elements(*self.REMOVE_BTN)
        remove_button[0].click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BTN).click()
