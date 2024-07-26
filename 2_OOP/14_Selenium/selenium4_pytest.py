from selenium import webdriver
from selenium1 import make_screenshot
from selenium2_POM import LoginPage
import time
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]


@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    assert driver.current_url == "https://www.saucedemo.com/"
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == url, make_screenshot(driver)
    except AssertionError:
        print("Logowanie, nie powiodło się")
        raise
    else:
        print("Logowanie poprawne")
    finally:
        print('koniec')
        driver.quit()
