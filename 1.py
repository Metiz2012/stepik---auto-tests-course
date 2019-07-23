from selenium import webdriver
driver = webdriver.Chrome()
link = 'https://mail.ru/'
driver.get(link)
y=driver.find_element_by_name("clb1797086").text
print(y)

