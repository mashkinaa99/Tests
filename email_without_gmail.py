from selenium import webdriver
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://www.olx.ua/')

    create_post = driver.find_element_by_id('postNewAdLink')
    create_post.click()

    reg = driver.find_element_by_xpath('//*[@id="innerLayout"]/section/div/div/nav/ul/li[2]')
    reg.click()

    mail_input = driver.find_element_by_id('userEmailPhoneRegister')
    mail_input.send_keys('aaaaaaa@.com')

    checkbox = driver.find_element_by_class_name('login-form__checkbox')
    checkbox.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-form__checkbox')))
    checkbox.click()

    log = driver.find_element_by_id('button_register')
    log.click()

    error = driver.find_elements_by_xpath("//*[contains(text(), 'Неправильный формат email или номера телефона')]")
    if len(error) <= 0:
        print('ERROR email_without_gmail: Phone or mail adopted aaaaaaa@.com')
    else:
        print('email_without_gmail OK')

    driver.quit()


except Exception:
    print('ERROR: \n' + traceback.format_exc())
