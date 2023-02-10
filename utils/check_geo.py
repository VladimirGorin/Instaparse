from selenium.webdriver.common.by import By
import time
from __PATHS import stories_post, stories_post_canvas , stories_post_canvas, stories_geo_search_scroll_block, stories_geo_search_tag_name, stories_geo_search_input, stories_geo_search, stories_geo_search_tag_name_input
from get_posts import get_posts_catalog
from clear_notifications import clear_notifications
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


def get_stories_geo(browser, geoTag, like_limit, stories_search, step):
    clear_notifications(browser)
    for g in geoTag:

        hrefs = []
        i = 0
        for elements_ in browser.find_elements(By.TAG_NAME, stories_geo_search_tag_name):
            if i == 2:
                elements_.click()
                i += 1
            i += 1
        time.sleep(2)
        for elements_ in browser.find_elements(By.TAG_NAME, stories_geo_search_tag_name_input):
            if elements_.get_attribute("placeholder") == stories_geo_search_input:
                elements_.send_keys(g)

        time.sleep(2)
        i = 0
        while i < stories_search:
            browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', browser.find_element(By.CLASS_NAME, stories_geo_search_scroll_block))
            time.sleep(5)
            browser.execute_script(f"document.querySelector('.{stories_geo_search_scroll_block}').scrollTo(0, screenTop);")
            time.sleep(5)

            i += 1

        for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{stories_geo_search}')]//child::*"):
            if elements_.tag_name == "a":
                href = elements_.get_attribute("href")
                if href != None:  # geotags_links
                    if "/explore/locations/" in href:
                        hrefs.append(href)

        for l in hrefs:
            browser.get(l)
            time.sleep(2)

            links = []
            i = 0
            while i < stories_search:
                print(i)
            
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
                browser.execute_script("window.scrollTo(200, document.body.scrollTop);")                
                time.sleep(5)
                i+=1

            time.sleep(2)
            try:
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


            for l in links:
                browser.get(l)
                time.sleep(4)
                try:
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

