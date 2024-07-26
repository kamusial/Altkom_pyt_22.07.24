from selenium import webdriver
from selenium2_POM import LoginPage
from selenium1 import make_screenshot
import time

def test_login_page():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    assert driver.current_url == "https://www.saucedemo.com/"
    page.enter_username('standard_user')
    page.enter_password('secret_sauce')
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == "https://www.saucedemo.com/inventory.htmll", make_screenshot(driver)
    except AssertionError:
        print("Logowanie, nie powiodło się")
        raise
    else:
        print("Logowanie poprawne")
    finally:
        print('koniec')
        driver.quit()





