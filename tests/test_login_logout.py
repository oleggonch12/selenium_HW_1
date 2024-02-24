import time
from pages import LoginAdminPage
from selenium.webdriver.common.by import By


def test_login_logout(slow_down_tests, browser):
    browser.get(browser.base_url + "/administration")
    username = browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    username.send_keys('user')
    password = browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    password.send_keys('bitnami')
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    time.sleep(1)
    expected_url_login = browser.base_url + '/administration/index.php?route=common/dashboard&user_token='
    current_url_login = browser.current_url
    browser.find_element(By.XPATH, '//*[@id="nav-logout"]/a').click()
    time.sleep(1)
    expected_url_logout = browser.base_url + '/administration/index.php?route=common/login'
    current_url_logout = browser.current_url

    assert current_url_login.startswith(expected_url_login) and expected_url_logout == current_url_logout
