from selenium.webdriver.common.by import By
import time
from __PATHS import user_profile_followers_body
from clear_notifications import clear_notifications
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from itertools import groupby
from utils.analytics_functions.get_analytics import get_analytics

def get_users(browser, subTag, scroll_analytic, users_parse):
    clear_notifications(browser)
    for u in subTag:
        print(subTag)
        browser.get(f"https://instagram.com/{u}/followers/")
        time.sleep(8)

        hrefs = []
        users = []
        i = 0

        while i < scroll_analytic:
            try:
                
                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', browser.find_element(By.CLASS_NAME, user_profile_followers_body))
                time.sleep(5)
                browser.execute_script(f"document.querySelector('.{user_profile_followers_body}').scrollTo(0, screenTop);")
                time.sleep(5)
                i+=1
            except NoSuchElementException:
                print("Элемент скрол бар не найден")
                continue
        
        try:

            for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{user_profile_followers_body}')]//child::*"):
                if elements_.tag_name == "a":
                    href = elements_.get_attribute("href")
                    if href != None:
                        hrefs.append(href)
            
        except NoSuchElementException:
            print("Элемент скрол бар не найден")
            continue
        except StaleElementReferenceException:
            print("Элемент устарел пробуем заново")
            pass

        for l in hrefs:
            link = l.replace("https://www.instagram.com/", "")
            link = link.split("/")[0]
            users.append(link)

        browser.close()
        browser.quit()

        get_analytics([el for el, _ in groupby(users)], users_parse)
