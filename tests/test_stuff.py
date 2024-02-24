import time
from selenium.webdriver.common.by import By


def test_camera(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]/a').click()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/h4/a').click()
    header = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/h1').text
    price_old = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/span').text
    price_new = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[2]/h2/span').text

    assert header == 'Canon EOS 5D' and price_old == '$122.00' and price_new == '$98.00', \
        "Карточка неверно отображается"


def test_laptop(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/a').click()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/h4/a').click()
    header = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/h1').text
    price = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2/span').text

    assert header == 'HP LP3065' and price == '$122.00', "Карточка неверно отображается"


def test_phones(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[6]/a').click()
    elements = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(elements) == 3, "Количество телефонов не сооветствует"


def test_tablets(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[4]/a').click()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/h4/a').click()
    header = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1').text
    price = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2/span').text

    assert header == 'Samsung Galaxy Tab 10.1' and price == '$241.99', "Карточка неверно отображается"


def test_monitors(browser):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/div/div/ul/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/h4/a').click()
    header = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1').text
    price_old = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/span').text
    price_new = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[2]/h2/span').text

    assert header == 'Apple Cinema 30"' and price_old == '$122.00' and price_new == '$110.00', \
        "Карточка неверно отображается"
