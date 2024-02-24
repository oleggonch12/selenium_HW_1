import random
import string
from selenium.webdriver.common.by import By


def gen_user():
    return {
        "first_name": ''.join(random.choices(string.ascii_lowercase, k=6)),
        "last_name": ''.join(random.choices(string.ascii_lowercase, k=6)),
        "email": ''.join(random.choices(string.ascii_lowercase, k=5)) + '@' +
                 ''.join(random.choices(string.ascii_lowercase, k=4)) + '.ru',
        "password": ''.join(random.choices(string.ascii_lowercase, k=8))
    }


def test_registration(browser):
    user = gen_user()
    browser.get(browser.base_url + "/index.php?route=account/register")
    first_name = browser.find_element(By.XPATH, '//*[@id="input-firstname"]')
    first_name.send_keys(user['first_name'])
    last_name = browser.find_element(By.XPATH, '//*[@id="input-lastname"]')
    last_name.send_keys(user['last_name'])
    email = browser.find_element(By.XPATH, '//*[@id="input-email"]')
    email.send_keys(user['email'])
    password = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    password.send_keys(user['password'])
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button').click()

    assert browser.find_element(By.XPATH, '//*[@id="content"]/h1').text == 'Your Account Has Been Created!'
