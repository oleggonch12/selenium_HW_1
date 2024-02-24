import time
from selenium.webdriver.common.by import By
import pytest


def test_camera_catalog(slow_down_tests, browser):
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[7]/a').click()
    elements = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(elements) == 2, "Количество камер не сооветствует"


def test_laptop_catalog(slow_down_tests, browser):
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/a').click()
    elements = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(elements) == 5, "Количество лэптопов не сооветствует"


def test_phones_catalog(slow_down_tests, browser):
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[6]/a').click()
    elements = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(elements) == 3, "Количество телефонов не сооветствует"


def test_mp3_players_catalog(slow_down_tests, browser):
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[8]/a').click()
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[8]/div/a').click()
    elements = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(elements) == 4, "Количество MP3-плееров не сооветствует"


@pytest.mark.xfail
def test_non_existence_software_catalog(slow_down_tests, browser):
    browser.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[5]/a').click()
    elements = browser.find_elements(By.CLASS_NAME, "col.mb-3")

    assert len(elements) == 4, "Количество программ не сооветствует"
