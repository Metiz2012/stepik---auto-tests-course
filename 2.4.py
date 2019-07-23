from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import math
def calc(x) :
    return(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)

summa = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000")
    )
driver.find_element_by_class_name("btn-primary").click()

answer = driver.find_element_by_id("answer")
driver.execute_script("return arguments[0].scrollIntoView(true);", answer)


x = int(driver.find_element_by_id("input_value").text)
y=str(calc(x))

answer.send_keys(y)

#driver.find_element_by_id("answer").send_keys(y)

driver.find_element_by_id("solve").click()
message = driver.find_element_by_id("check_message")
assert 'успешно' in message.text
driver.switch_to.alert