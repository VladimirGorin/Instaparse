import time
import random
from selenium.webdriver.common.by import By
from __PATHS import login_input_email, login_input_pass
from selenium.webdriver.common.keys import Keys
from clear_notifications import clear_notifications
from get_code import get_the_email_code
from selenium.common.exceptions import NoSuchElementException

def login(browser, email, password, check_name_exists):

    browser.get('https://www.instagram.com')

    time.sleep(random.randrange(5, 7))

    print(email, password)

    try: 
        browser.find_element(By.NAME, login_input_email).send_keys(email)
        send = browser.find_element(By.NAME, login_input_pass)
        print(send.text)

        send.send_keys(password)
        send.send_keys(Keys.ENTER)
        
        time.sleep(6)
        get_the_email_code(browser)
        time.sleep(6)
        clear_notifications(browser)
    except NoSuchElementException:
        print("Авторизация не успешна")

