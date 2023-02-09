from selenium import webdriver
from selenium.webdriver.common.by import By
from settings.data import get_user_settings, get_user_analytics
from utils.check_geo import get_stories_geo
from utils.check_hastage import get_stories_hastage
from utils.check_sub import get_stories_sub
from utils.get_analytics import get_analytics
from utils.get_on_sub import get_on_sub
from generate_files import generate_files
from login import login
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import json

print("\n1 = Только по step без конечно\n2 = Только по кокретному аккаунту без конечно\n")
get_step = input("Введите функцию: ")


if int(get_step) == 1:
    input_step = input("Введите step: ")
    
    while True:
        for u in get_user_settings():
            
            email = u['email']
            password = u['pass']
            step = u['step']
            hasTag = u["hastages"]
            geoTag = u["geolocation"]
            subTag = u["subscriber"]
            stories = u["stories"]
            stories_search = u["stories_search"]
            stories_sub = u["stories_sub"] 
            sub = u["sub"] 
            sub_scroll = u["sub_scroll"]
            like_limit = u["like_limit"]
            ingore = u["on_sub"]
            scroll_on_sub = u["scroll_on_sub"]


            try:
                # try:
                    if input_step == "1":
                        if str(step) == input_step:
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 1')
                            login(browser, email, password)
                            get_stories_hastage(browser, hasTag, like_limit, stories)
                    if input_step == "2":
                        if str(step) == input_step:
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 2')
                            login(browser, email, password)
                            get_stories_geo(browser, geoTag, like_limit, stories_search)
                    if input_step == "3":
                        if str(step) == input_step:
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 3')
                            login(browser, email, password)
                            get_stories_sub(browser, subTag, like_limit, stories_sub)
                    if input_step == "4":
                        if str(step) == input_step:
                            print('step 4')
                            get_analytics(sub, email, password)
                    if input_step == "5":
                        if str(step) == input_step:
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 5')
                            login(browser, email, password)
                            get_on_sub(browser, ingore, get_user_analytics(), email, scroll_on_sub)
                    
                    if input_step == "6":
                        print('step 6')
                        generate_files()

                    elif step == None:
                        ""
                    else:
                        print(f"В базе не было найдено объекта с шагом {input_step}")
                # except StaleElementReferenceException:
                #     print("Забытый элемент")
                #     continue
            except NoSuchElementException:
                pass
            except ElementNotInteractableException:
                pass
elif int(get_step) == 2:
    input_step = input("Введите уникальный ID: ")

    while True:
        for u in get_user_settings():
            email = u['email']
            password = u['pass']
            step = str(u['step'])
            hasTag = u["hastages"]
            geoTag = u["geolocation"]
            subTag = u["subscriber"]
            stories = u["stories"]
            stories_search = u["stories_search"]
            stories_sub = u["stories_sub"] 
            sub = u["sub"] 
            sub_scroll = u["sub_scroll"]
            auth_id = str(u["auth_id"])
            like_limit = u["like_limit"]
            ingore = u["on_sub"]
            scroll_on_sub = u["scroll_on_sub"]

            print(input_step, auth_id)
            try:
                # try:
                    if input_step == auth_id:
                        if step == "1":
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 1')
                            login(browser, email, password)
                            get_stories_hastage(browser, hasTag, like_limit, stories)
                        if step == "2":
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 2')
                            login(browser, email, password)
                            get_stories_geo(browser, geoTag, like_limit, stories_search)
                        if step == "3":
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 3')
                            login(browser, email, password)
                            get_stories_sub(browser, subTag, like_limit, stories_sub)
                        if step == "4":
                            print('step 4')
                            get_analytics(sub, email, password)
                        if step == "5":
                            browser = webdriver.Chrome("./chromedriver/chromedriver.exe")

                            print('step 5')
                            login(browser, email, password)
                            get_on_sub(browser, ingore, get_user_analytics(), email, scroll_on_sub)
                        if step == "6":
                            print('step 6')
                            generate_files()

                        elif step == None:
                            ""
                    elif step == None:
                        ""
                    else:
                        print(f"В базе не было найдено объекта с auth_id - {input_step}")
                # except StaleElementReferenceException:
                #     print("Забытый элемент")
                #     continue
            except NoSuchElementException:
                pass
            except ElementNotInteractableException:
                pass
else:
    print("Функция не обронужена :(") 