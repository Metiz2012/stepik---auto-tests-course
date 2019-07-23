from selenium import webdriver
driver = webdriver.Chrome()
import math

def calc(x) :
    return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)
driver.find_element_by_class_name("btn-primary").click()
confirm=driver.switch_to.alert
confirm.accept()

x=int(driver.find_element_by_id("input_value").text)
y=str(calc(x))

driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_class_name("btn-primary").click()

alert=driver.switch_to.alert
alert_text=alert.text
print(alert_text)
alert.accept()

