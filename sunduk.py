from selenium import webdriver
import math
driver=webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")

#Функция вычисления X
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


sunduk=driver.find_element_by_css_selector("#treasure")
a_checked=sunduk.get_attribute("valuex")
y=calc(a_checked)

stroka=driver.find_element_by_xpath("//input[@id='answer']").send_keys(y)
galka=driver.find_element_by_xpath("//input[@id='robotCheckbox']").click()
galka2=driver.find_element_by_css_selector("#robotsRule").click()
knopka=driver.find_element_by_class_name("btn-default").click()

