from pages.cart_page import CartPage

def test_correlation_num_items_badge(checkout_driver):
    page = CartPage(checkout_driver)
    number_of_items = page.get_item_count()
    number_of_badge = page.get_cart_badge_count()
    assert int(number_of_badge) == int(number_of_items)

def test_button_remove(checkout_driver):
    page = CartPage(checkout_driver)
    number_of_items_before_remove = page.get_item_count()
    page.remove_first_item()
    number_of_items_after_remove = page.get_item_count()
    assert int(number_of_items_before_remove) - 1 == int(number_of_items_after_remove)


def test_checkout_button(checkout_driver):
    page = CartPage(checkout_driver)
    page.click_checkout()
    assert "checkout-step-one" in checkout_driver.current_url


def test_continue_shopping_button(checkout_driver):
    page = CartPage(checkout_driver)
    page.click_continue_shopping()
    assert "inventory" in checkout_driver.current_url



