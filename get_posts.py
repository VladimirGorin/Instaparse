from selenium.webdriver.common.by import By
import time
from __PATHS import stories_post_like, stories_counter, stories_view_count
from info_tracker import get_info
import datetime
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

def get_posts_catalog(browser, state, user, step, email):
    time.sleep(4)
    
    url = browser.current_url 


    if url != "https://www.instagram.com/":
        if url != f"https://www.instagram.com/{email}":
            now = datetime.datetime.now()

            print("get_posts")
            i = 0
            
            for elements_ in browser.find_elements(By.TAG_NAME, "button"):
                try:
                    if i == 0:
                        elements_.click()  
                        i+=1
                    i+=1
                except ElementClickInterceptedException:
                    print("Мы не можем нажать на элемент")
                    pass

            time.sleep(3)
            i = 0

            status = {
                "likes": 0,
                "stories_viewed": 0
            }

            if state:
                for elements_ in browser.find_elements(By.CLASS_NAME, stories_post_like):
                    try:
                        if i == 3:
                            elements_.click()
                            status["likes"] = 1
                            i+=1
                        i+=1
                    except ElementClickInterceptedException:
                        print("Мы не можем нажать на элемент")
                        pass
            
            try:
                for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{stories_counter}')]//child::*"):
                    if elements_.get_attribute("class") == stories_view_count:
                        status["stories_viewed"]+=1
            except StaleElementReferenceException:
                print("Элемент устарел, пробуем заново")
                pass

            get_info(step, email, status["likes"], status["stories_viewed"], 0, now.strftime("%d-%m-%Y %H:%M"))

            print("Спим 3 минуты")
            time.sleep(180)                
