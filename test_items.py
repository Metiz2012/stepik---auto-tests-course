import time
def test_find__card_button(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    btn= browser.find_element_by_css_selector(".btn-add-to-basket")
    assert btn.is_displayed(), "Че то не то в тесте"
