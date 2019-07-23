from selenium import webdriver
driver = webdriver.Chrome()
import math
import  time

def calc(x) :
    return math.log(abs(12*math.sin(x)))

link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)
driver.find_element_by_class_name("btn-primary").click()

#Переключение на новую вкладку
new_window=driver.window_handles[1]
driver.switch_to.window(new_window)
time.sleep(1)
#Вычисление f(x)
x = int(driver.find_element_by_css_selector("#input_value.nowrap").text)
y = str(calc(x))

driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_class_name("btn-primary").click()

alert=driver.switch_to.alert
alert_text=alert.text
print(alert_text)
alert.accept()

