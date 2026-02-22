from pages.login_page import LoginPage


def test_login_valido(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_password_errata(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "password_errata")
    assert "Epic sadface" in page.get_error_message()

def test_login_utente_bloccato(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "locked out." in page.get_error_message()