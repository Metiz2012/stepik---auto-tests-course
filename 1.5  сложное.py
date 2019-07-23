from selenium import webdriver
import time
link="http://suninjuly.github.io/registration2.html"
driver=webdriver.Chrome()
driver.get(link)

#Код который заполняет обязательные поля

Firstname=driver.find_element_by_xpath("//div[@class='form-group first_class']//input[@placeholder='Введите имя']").send_keys('Name')
time.sleep(1)
Lastname=driver.find_element_by_xpath("//div[@class='form-group second_class']//input[@placeholder='Введите фамилию']").send_keys('lastname')
time.sleep(1)
Email=driver.find_element_by_xpath("//div[@class='form-group third_class']//input[@placeholder='Введите Email']").send_keys('2@mail.ru')
time.sleep(1)
secondblock=driver.find_elements_by_xpath("//div[@class='second_block']//input[@class]")

for i in secondblock:
    i.send_keys("ggggjjjjjj")
    time.sleep(1)

# Отправляем заполненную форму
bottom=driver.find_element_by_class_name("btn-default").click()

# Проверяем, что смогли зарегистрироваться
# Ждем загрузки страницы
time.sleep(1)

# Находим элемент, содержащий текст
welcome_text_elt=driver.find_element_by_xpath("//div[contains(@class,'container')]")

# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

