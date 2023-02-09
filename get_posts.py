from selenium.webdriver.common.by import By
import time
from __PATHS import stories_post_like

def get_posts_catalog(browser, state, user):
    time.sleep(3)
    
    url = browser.current_url 


    if url != "https://www.instagram.com/" and url != f"https://www.instagram.com/{user}":
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
                    i+=1
                i+=1

        print("Спим 3 минуты")
        time.sleep(180)                
