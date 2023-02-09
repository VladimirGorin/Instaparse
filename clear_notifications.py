import time
from selenium.webdriver.common.by import By
from __PATHS import notification_button, notification_text
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def clear_notifications(browser):
        browser.get('https://www.instagram.com')
        time.sleep(4)

        try:
            for elements_ in browser.find_elements(By.TAG_NAME, notification_button):
                text1 = elements_.text
                if text1 == notification_text:
                    elements_.click()

        except StaleElementReferenceException:
            print("Елемент на сайте не был найден пробуем заново")
            pass  

        except NoSuchElementException:
            print("Елемент не найден")  
        
        time.sleep(6)