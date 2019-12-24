'''
1. Open the link http://suninjuly.github.io/math.html.
2. Read value for the variable x.
3. Calculate x by using function below "def calc(x)".
4. Put your answer into the text field.
5. Mark checkbox "I'm the robot".
6. Select radiobutton "Robots rule!".
7. Click button Submit.
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