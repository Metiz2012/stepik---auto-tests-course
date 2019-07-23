

from selenium import webdriver
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
driver.get(link)
import  os

driver.find_element_by_name("firstname").send_keys('dfdf')
driver.find_element_by_name("lastname").send_keys('cvx')
driver.find_element_by_name("email").send_keys('vbxgf')

element=driver.find_element_by_name("file")
curent_dir = os.path.abspath(os.path.dirname("C:/Users/ibelousov/Desktop/"))
file_path = os.path.join(curent_dir,'file.txt')
element.send_keys(file_path)

driver.find_element_by_css_selector(".btn-primary").click()

alert = driver.switch_to.alert
z=alert.text
print(z)
alert.accept()



