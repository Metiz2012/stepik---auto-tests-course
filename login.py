import time

              # webdriver это и есть набор команд для управления браузером
from selenium import webdriver
              #инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
              # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)


              # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/8?auth=login&unit=196192")
time.sleep(2)
Login_write=driver.find_element_by_name("login")
Login_write.send_keys("metiz2012@mail.ru")

Password_write=driver.find_element_by_css_selector('#id_login_password.sign-form__input')
Password_write.send_keys('4r7u8m1c')

Login_button = driver.find_element_by_xpath ("//form[@id='login_form']/button").click()



              # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
              # Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

