import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_basket_is_available(browser):
    browser.get(link)
    driver_wait = WebDriverWait(browser, 10)

    add_to_basket_button = None
    try:
        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except selenium.common.exceptions.NoSuchElementException:
        add_to_basket_button = False

    assert add_to_basket_button, 'There is no "add to basket" button available!'
