import time
from selenium.webdriver.common.by import By


def test_pop_up_basket(slow_down_tests, browser):
    basket_button = browser.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    basket_button.click()
    pop_up_menu = browser.find_element(By.CSS_SELECTOR, "#header-cart > div > ul")

    assert pop_up_menu.text == "Your shopping cart is empty!", "Не отрабатывает кнопка корзины"


def test_main_page_featured_items(slow_down_tests, browser):
    featured_items = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(featured_items) == 4, "Неверное количество продуктов в блоке featured"


def test_currency_set_up(slow_down_tests, browser):
    currency_button = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    currency_button.click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a').click()
    element_euro = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    text_element_euro = element_euro.text
    currency_button = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    currency_button.click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a').click()
    element_pounds = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    text_element_pounds = element_pounds.text
    currency_button = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span')
    currency_button.click()
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/a').click()
    element_dollars = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    text_element_dollars = element_dollars.text

    assert (text_element_euro.endswith('€') and text_element_pounds.startswith('£') and
            text_element_dollars.startswith('$')), 'Неправильно выставляются валюты'


def test_amount_of_brands(slow_down_tests, browser):
    amount = len(browser.find_elements(By.CLASS_NAME, "col-2.text-center"))

    assert amount == 11, "Неправильное количество спонсоров"


def test_amount_of_photo(slow_down_tests, browser):
    amount = len(browser.find_elements(By.CLASS_NAME, "fa-solid.fa-chevron-right"))

    assert amount == 2, "Неправильное количество изображений"
