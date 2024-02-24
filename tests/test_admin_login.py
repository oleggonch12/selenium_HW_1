from pages import LoginAdminPage
import time


def test_login_page_external(browser):
    browser.get(browser.base_url + "/administration")
    username = browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    username.send_keys('user')
    password = browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    password.send_keys('bitnami')
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    time.sleep(1)
    expected_url = browser.base_url + '/administration/index.php?route=common/dashboard&user_token='
    current_url = browser.current_url

    assert current_url.startswith(expected_url)
