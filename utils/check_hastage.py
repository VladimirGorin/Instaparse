from selenium.webdriver.common.by import By
import time
from __PATHS import stories_post, stories_post_canvas
from get_posts import get_posts_catalog
from clear_notifications import clear_notifications
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


def get_stories_hastage(browser, has_tags, like_limit, stories, step):
    clear_notifications(browser)
    for h in has_tags:
        
        browser.get(f"https://www.instagram.com/explore/tags/{h}/")

        time.sleep(2)

        links = []
        i = 0
        while i < stories:
            print(i)
            browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")
            time.sleep(5)
            browser.execute_script("window.scrollTo(200, document.body.scrollTop);")
            time.sleep(5)
            
            i+=1

        try:
            time.sleep(2)
            for element in browser.find_elements(By.XPATH, f"//div[contains(@class, '{stories_post}')]//child::*"):
                href = element.get_attribute("href")
                if href != None:
                    links.append(href)
        except StaleElementReferenceException:
            print("Елемент на сайте не был найден пробуем заново")
            pass  
        except NoSuchElementException:
            print("Елемент не найден")  
            continue

        try:
            for l in links:
                browser.get(l)
                time.sleep(4)
                for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{stories_post_canvas}')]//child::*"):
                    if elements_.tag_name == "a":
                        print(elements_.text)
                        user = elements_.text

                browser.get(f"https://www.instagram.com/stories/{user}")
                time.sleep(2)
                get_posts_catalog(browser, True, l, step) 

        except StaleElementReferenceException:
            print("Елемент на сайте не был найден пробуем заново")
            pass  
        except NoSuchElementException:
            print("Елемент не найден")  
            continue
        
        time.sleep(5)
