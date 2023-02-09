from selenium.webdriver.common.by import By
import time
from clear_notifications import clear_notifications
from get_posts import get_posts_catalog
from __PATHS import user_profile_followers_body
from itertools import groupby
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


def get_stories_sub(browser, subTag, like_limit, stories_sub):
    time.sleep(3)
    clear_notifications(browser)
    for s in subTag:
        print(s)

        browser.get(f"https://www.instagram.com/stories/{s}")
        time.sleep(3)
        get_posts_catalog(browser, False, s) 

        hrefs = []
        browser.get(f"https://www.instagram.com/{s}/followers")
        time.sleep(4)

        i = 0
        while i < stories_sub:
            browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', browser.find_element(By.CLASS_NAME, user_profile_followers_body))
            time.sleep(5)
            browser.execute_script(f"document.querySelector('.{user_profile_followers_body}').scrollTo(0, screenTop);")
            time.sleep(5)

            i+=1 
            
        try:

            for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{user_profile_followers_body}')]//child::*"):
                if elements_.tag_name == "a":
                    hrefs.append(elements_.get_attribute('href').replace("https://www.instagram.com/", ""))

            new_hrefs = [el for el, _ in groupby(hrefs)]
                    
            for l in new_hrefs:
                stories = f"https://www.instagram.com/stories/{l}"
                browser.get(stories)
                time.sleep(4)
                get_posts_catalog(browser, True, l) 

        except StaleElementReferenceException:
            print("Елемент на сайте не был найден пробуем заново")
            pass  
        except NoSuchElementException:
            print("Елемент не найден")  
            continue
            
            
