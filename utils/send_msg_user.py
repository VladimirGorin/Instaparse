from clear_notifications import clear_notifications
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from __PATHS import direct_profile
from clear_notifications import clear_notifications
import time
from info_tracker import get_info
import datetime


def send_message(browser, message, msg_limit, step, user):
    clear_notifications(browser)
    browser.get("https://www.instagram.com/direct/inbox/")
    time.sleep(4)
    hrefs = []
    i = 0

    try:
        for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{direct_profile}')]//child::*"):
            try:
                if elements_.tag_name == "a":
                    if msg_limit < i:
                        hrefs.append(elements_.get_attribute("href"))
                    i += 1
            except StaleElementReferenceException:
                print("Елемент на сайте не был найден пробуем заново")
                pass
    except NoSuchElementException:
        print("Елемент не найден")


    for href in hrefs:
        browser.get(href)
        time.sleep(7)
        try:
            now = datetime.datetime.now()

            textarea = browser.find_element(By.TAG_NAME, "textarea")
            textarea.send_keys(message)
            time.sleep(2)
            textarea.send_keys(Keys.ENTER)

            get_info(step, user, 0, 0, 1, now.strftime("%d-%m-%Y %H:%M"))
        except NoSuchElementException:
            print("Елемент не найден")

        except ElementNotInteractableException:
            print("Не возможно кликнуть на элемент, пробуем заново")
            pass
