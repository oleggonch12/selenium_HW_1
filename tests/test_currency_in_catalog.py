from selenium.webdriver.common.by import By


def test_currency_in_catalog(slow_down_tests, browser):
    # test euro
    euro = []
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]').click()
    euro.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/div/div/span[1]').text)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[4]/a').click()
    euro.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]').text)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/a').click()
    euro.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]').text)

    # test_pound
    pound = []
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a').click()
    pound.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]').text)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]/a').click()
    pound.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/div/div/span[1]').text)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[4]/a').click()
    pound.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]').text)

    # test_dollar
    dollar = []
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/a').click()
    dollar.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]').text)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]/a').click()
    dollar.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/div/div/span[1]').text)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/a').click()
    dollar.append(browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]').text)

    assert len([i for i in dollar if i.startswith('$')]) == 3 and len([i for i in pound if i.startswith('£')]) == 3 \
           and len([i for i in euro if i.endswith('€')]) == 3, 'Неправильно выставляются валюты'