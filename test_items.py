from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time



def test_guest_should_see_login_link(browser,zara):
    browser.get(link)
    knopka =WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-add-to-basket')))
    knopka.click()

    browser.implicitly_wait(1)
    text= browser.find_element_by_css_selector("div.alertinner").text
    assert text == "был добавлен в вашу корзину.", "Че то не то в тесте"
