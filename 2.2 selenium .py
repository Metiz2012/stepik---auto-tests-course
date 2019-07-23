from selenium import webdriver
driver = webdriver.Chrome()
link="http://suninjuly.github.io/selects1.html"
driver.get(link)
from selenium.webdriver.support.ui import Select



a=int(driver.find_element_by_css_selector("#num1.nowrap").text)
b=int(driver.find_element_by_css_selector("#num2.nowrap").text)
dab = str((a)+(b))
select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(dab)

driver.find_element_by_class_name("btn-default").click()


