from selenium.webdriver.common.by import By
import time
from __PATHS import stories_post_like
from info_tracker import get_info
import datetime

def get_posts_catalog(browser, state, user, step):
    time.sleep(4)
    
    url = browser.current_url 


    if url != "https://www.instagram.com/":
        if url != f"https://www.instagram.com/{user}":
            now = datetime.datetime.now()

            print("get_posts")
            i = 0
            
            for elements_ in browser.find_elements(By.TAG_NAME, "button"):
                if i == 0:
                    elements_.click()  
                    i+=1
                i+=1

            time.sleep(3)
            i = 0

            if state:
                for elements_ in browser.find_elements(By.CLASS_NAME, stories_post_like):
                    if i == 3:
                        elements_.click()
                        get_info(step, user, 1, 1, 0, now.strftime("%d-%m-%Y %H:%M"))
                        i+=1
                    i+=1

            print("Спим 3 минуты")
            time.sleep(180)                
