'''
1. Открыть страницу http://suninjuly.github.io/math.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x (код для этого приведён ниже).
4. Ввести ответ в текстовое поле.
5. Отметить checkbox "I'm the robot".
6. Выбрать radiobutton "Robots rule!".
7. Нажать на кнопку Submit.
'''

########### My resolution ###############

from selenium import webdriver
import time, math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)

    answer = browser.find_element_by_id('answer').send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox').click()
    option2 = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to.alert.text
    print(alert.split()[-1])

finally:
    time.sleep(10)
    browser.quit()