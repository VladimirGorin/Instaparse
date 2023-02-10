from selenium.webdriver.common.by import By
import time
from __PATHS import user_profile_followers_body, me_profile_button
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
from clear_notifications import clear_notifications


def confirm_delete(browser):
    for elements_ in browser.find_elements(By.CLASS_NAME, "_a9--"):
        try:
            if elements_.tag_name == "button":
                if elements_.text == "Удалить":
                    elements_.click()
                    break
        except ElementClickInterceptedException:
            print("Мы не можем нажать на элемент")

            pass                
def get_on_sub(browser, ingore, users, email, scroll_on_sub):
    clear_notifications(browser)    

    browser.get(f"https://www.instagram.com/{email}/followers/")
    time.sleep(8)

    i = 0

    while i < scroll_on_sub:       
            print(i)
            
            browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', browser.find_element(By.CLASS_NAME, user_profile_followers_body))
            time.sleep(5)
            browser.execute_script(f"document.querySelector('.{user_profile_followers_body}').scrollTo(0, screenTop);")
            time.sleep(5)
            i+=1
        
    for u in users:
            user_settings = [{
                "status": False,
                "delete_status": False
            }]

            print(u["user"], f'{ingore} {u[ingore]}')
            try: 
                for elements_ in browser.find_elements(By.XPATH, f"//div[contains(@class, '{user_profile_followers_body}')]//child::*"):
                    tag = elements_.tag_name
                    if tag == "a":
                        a = elements_.get_attribute("href").replace("https://www.instagram.com/", "")
                        href = a.replace("/", "")
                        if href == u["user"]:
                            if ingore == "active":
                                if u[ingore] == "last post 3 months ago":
                                    user_settings[0]["status"] = True

                            if u[ingore] == False:
                                    user_settings[0]["status"] = True

                            if u[ingore] == None:
                                    user_settings[0]["status"] = False

                            if user_settings[0]["status"] != True:
                                break
                    if tag == "button":
                        if elements_.text == me_profile_button:
                            if user_settings[0]["status"]:
                                if user_settings[0]["delete_status"] == False:
                                    try:
                                        user_settings[0]["delete_status"] = True
                                        
                                        elements_.click()
                                        time.sleep(2)
                                        confirm_delete(browser)
                                    except ElementClickInterceptedException:
                                        print("Мы не можем нажать на элемент")
                                        pass

            except StaleElementReferenceException:
                print("Елемент на сайте не был найден пробуем заново")
                pass  
            except NoSuchElementException:
                print("Елемент не найден")  
                continue
            
            if user_settings[0]["delete_status"]:
                print("Спим 10 минуты")
                time.sleep(600)
