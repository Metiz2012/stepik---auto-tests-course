from selenium import webdriver
driver = webdriver.Chrome()
import math

def calc(x) :
    return math.log(abs(12*math.sin(x)))


link="http://SunInJuly.github.io/execute_script.html"
driver.get(link)
x=int(driver.find_element_by_css_selector('#input_value.nowrap').text)

y=str(calc(x))

button=driver.find_element_by_css_selector(".btn-default")
pole=driver.find_element_by_css_selector("#answer.form-control").send_keys(y)
driver.find_element_by_css_selector("#robotCheckbox.form-check-input").click()
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
driver.find_element_by_css_selector("#robotsRule.form-check-input").click()
button.click()
