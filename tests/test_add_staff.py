import time

from selenium.webdriver.common.by import By


def test_add_stuff_to_basket(slow_down_tests, browser):

    element_1 = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div/button[1]')
    browser.execute_script("arguments[0].click();", element_1)
    element_2 = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[2]/form/div/button[1]')
    browser.execute_script("arguments[0].click();", element_2)
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="input-option-226"]/option[2]').click()
    browser.find_element(By.XPATH, '//*[@id="button-cart"]').click()
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button').click()
    browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/ul/li/div/p/a[1]/strong').click()
    rows = browser.find_elements(By.CLASS_NAME, 'table.table-bordered')
    first_prod = browser.find_element(By.XPATH, '//*[@id="shopping-cart"]/div/table/tbody/tr[1]/td[2]/a').text
    second_prod = browser.find_element(By.XPATH, '//*[@id="shopping-cart"]/div/table/tbody/tr[2]/td[2]/a').text
    assert len(rows) == 2 and first_prod == 'Canon EOS 5D' and second_prod == 'iPhone'
