from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")

name = browser.find_element_by_css_selector('div.first_block  div:nth-child(1) input')
name.send_keys("Konstantin")
name.click()
surname = browser.find_element_by_css_selector('div.first_block  div:nth-child(2) input')
surname.send_keys('Unknown')
surname.click()
e_mail = browser.find_element_by_css_selector('div.first_block  div:nth-child(3) input')
e_mail.send_keys('stepik@stepik.stepik')
e_mail.click()
browser.find_element_by_css_selector("button.btn").click()
welcome_text_elt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text