from selenium import webdriver
import math
link= "http://suninjuly.github.io/find_xpath_form"

driver=webdriver.Chrome()
driver.get(link)


elements=driver.find_elements_by_tag_name("input")

for i in elements:
    i.send_keys("Привет")


button1=driver.find_element_by_xpath("//div//button[text()='Отправить']").click()