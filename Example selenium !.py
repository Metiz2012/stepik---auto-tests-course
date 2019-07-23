from selenium import  webdriver
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/math.html")


x_element = driver.find_element_by_css_selector('#input_value.nowrap')
x = x_element.text


def calc(x) :
    return(math.log(abs(12*math.sin(int(x)))))
y=str(calc(x))

otvet=driver.find_element_by_css_selector("#answer.form-control").send_keys(y)
podtverjdenie = driver.find_element_by_id("robotCheckbox").click()
podtverjdenie2 = driver.find_element_by_id("robotsRule").click()
buttonz = driver.find_element_by_class_name("btn-default").click()