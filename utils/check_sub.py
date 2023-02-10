from selenium.webdriver.common.by import By
import time
from clear_notifications import clear_notifications
from get_posts import get_posts_catalog
from __PATHS import user_profile_followers_body
from itertools import groupby
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


def get_stories_sub(browser, subTag, like_limit, stories_sub, step, email):
    time.sleep(3)
    clear_notifications(browser)
    for s in subTag:
        try:
            stories = f"https://www.instagram.com/stories/{s}"
            browser.get(stories)
            time.sleep(4)
            get_posts_catalog(browser, True, s, step, email) 
        except StaleElementReferenceException:
            print("Елемент на сайте не был найден пробуем заново")
            pass  
        except NoSuchElementException:
            print("Елемент не найден")  
            continue
            
            
