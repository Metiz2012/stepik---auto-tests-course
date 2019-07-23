from selenium import webdriver
import time
link= "http://suninjuly.github.io/registration1.html"
driver=webdriver.Chrome()
driver.get(link)

#Код который заполняет обязательные поля

a=driver.find_element_by_xpath("//input[@type='text']")

