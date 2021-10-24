import time

import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_basket_is_available(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed(),\
        'There is no "add to basket" button available!'
