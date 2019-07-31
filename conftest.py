import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('language',["ru","en-gb","fr","es","ro","it","uk","pt"])
def zara(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
    return link
