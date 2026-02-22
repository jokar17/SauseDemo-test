from pages.information_page import InformationPage

def test_continue_checkout(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(name="nome", surname="cognome", zip=21100)
    assert "checkout-step-two" in information_driver.current_url

def test_back_checkout(information_driver):
    page = InformationPage(information_driver)
    page.click_cancel()
    assert "cart" in information_driver.current_url

def test_missed_name(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(surname="cognome", zip=21100)
    assert "First Name is required" in page.get_error_message()

def test_missed_surname(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(name="nome", zip=21100)
    assert "Last Name is required" in page.get_error_message()

def test_missed_zip(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(name="nome", surname="cognome")
    assert "Postal Code is required" in page.get_error_message()


def test_all_fields_empty(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form()
    assert "First Name is required" in page.get_error_message()


def test_only_name(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(name="nome")
    assert "Last Name is required" in page.get_error_message()


def test_only_surname(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(surname="cognome")
    assert "First Name is required" in page.get_error_message()


def test_only_zip(information_driver):
    page = InformationPage(information_driver)
    page.fill_checkout_form(zip=21100)
    assert "First Name is required" in page.get_error_message()