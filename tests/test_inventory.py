from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_select_order_az(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    page2 = InventoryPage(driver)
    page2.select_order("az")
    assert page2.get_titles_list() == sorted(page2.get_titles_list())


def test_select_order_za(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    page2 = InventoryPage(driver)
    page2.select_order("za")
    assert page2.get_titles_list() == sorted(page2.get_titles_list(), reverse=True)


def test_check_cart_number(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    page2 = InventoryPage(driver)
    page2.add_to_cart()
    assert int(page2.get_cart_number()) == 1

def test_check_cart_2(logged_driver):
    page = InventoryPage(logged_driver)
    page.add_to_cart()
    assert int(page.get_cart_number()) == 1





