from selenium import webdriver
from settings.data import get_user_settings, get_user_analytics
from utils.check_geo import get_stories_geo
from utils.check_hastage import get_stories_hastage
from utils.check_sub import get_stories_sub
from utils.analytics_functions.get_analytics import get_followees
from utils.analytics_functions.get_users import get_users
from utils.analytics_functions.get_on_sub import get_on_sub
from utils.send_msg_user import send_message
from login import login
from generate_files import generate_files_to_tracker, delete_files_to_tracker, generate_files, generate_files_analytic


def select_function():
    print("\n1 = Только по step без конечно\n2 = Только по кокретному аккаунту без конечно\n")
    get_step = input("Введите функцию: ")
    

    if int(get_step) == 1:
        input_step = input("Введите step: ")

        for u in get_user_settings():
            generate_files_to_tracker()
            delete_files_to_tracker()
            generate_files_analytic()
            generate_files()

            email = u['email']
            password = u['pass']
            step = u['step']

            hasTag = u["hastages"]
            geoTag = u["geolocation"]
            sub = u["analytic_sub"]
            subTag = u["subscribers"]

            stories = u["stories_hastag_scroll"]
            stories_search = u["stories_geo_scroll"]
            scroll_on_sub = u["scroll_on_sub"]
            scroll_analytic = u["scroll_analytic"]
            followes_scroll = u["followes_scroll"]


            users_parse = u["users_parse"]
            ingore = u["on_sub_category"]

            message_send = u["message_send"].encode("utf8").decode()
            print(message_send)
            msg_limit = u["msg_limit"]

            if input_step == "1":
                if str(step) == input_step:
                    while True:
                        browser = webdriver.Chrome(
                            "./chromedriver/chromedriver.exe")

                        print('step 1')
                        login(browser, email, password)
                        get_stories_hastage(browser, hasTag, stories, step, email)
            if input_step == "2":
                if str(step) == input_step:
                    while True:
                        browser = webdriver.Chrome(
                            "./chromedriver/chromedriver.exe")

                        print('step 2')
                        login(browser, email, password)
                        get_stories_geo(browser, geoTag, stories_search, step, email)
            if input_step == "3":
                if str(step) == input_step:
                    while True:
                        print('step 3')
                        users = get_followees(subTag, users_parse)
                        browser = webdriver.Chrome(
                            "./chromedriver/chromedriver.exe")
                        login(browser, email, password)
                        get_stories_sub(browser, users, step, email)
                        browser.quit()
                        browser.close()
                    
            if input_step == "4":
                if str(step) == input_step:
                    print('step 4')
                    browser = webdriver.Chrome("./chromedriver/chromedriver.exe")
                    login(browser, email, password)
                    get_users(browser, sub, scroll_analytic, users_parse, email)
            if input_step == "5":
                if str(step) == input_step:
                    browser = webdriver.Chrome(
                        "./chromedriver/chromedriver.exe")

                    print('step 5')
                    login(browser, email, password)
                    get_on_sub(browser, ingore, email, scroll_on_sub)
            if input_step == "6":
                while True:
                    print('step 6')
                    generate_files()
            if input_step == "7":
                if str(step) == input_step:
                    browser = webdriver.Chrome(
                        "./chromedriver/chromedriver.exe")

                    print('step 7')
                    login(browser, email, password)
                    send_message(browser, message_send,
                                 msg_limit, followes_scroll, step, email)
            elif step == None:
                ""
            else:
                print(
                    f"В базе не было найдено объекта с шагом {input_step}")

    elif int(get_step) == 2:
        input_step = input("Введите уникальный ID: ")
        for u in get_user_settings():
            generate_files_to_tracker()
            delete_files_to_tracker()
            generate_files_analytic()
            generate_files()

            email = u['email']
            password = u['pass']
            step = u['step']

            hasTag = u["hastages"]
            geoTag = u["geolocation"]
            sub = u["analytic_sub"]
            subTag = u["subscribers"]

            stories = u["stories_hastag_scroll"]
            stories_search = u["stories_geo_scroll"]
            scroll_on_sub = u["scroll_on_sub"]
            scroll_analytic = u["scroll_analytic"]
            followes_scroll = u["followes_scroll"]
            
            users_parse = u["users_parse"]
            ingore = u["on_sub_category"]
            message_send = u["message_send"]
            msg_limit = u["msg_limit"]
            auth_id = str(u["auth_id"])


            if auth_id == input_step:
                if str(step) == "1":
                    while True:
                        browser = webdriver.Chrome(
                            "./chromedriver/chromedriver.exe")

                        print('step 1')
                        login(browser, email, password)
                        get_stories_hastage(
                            browser, hasTag, stories, step, email)
                if str(step) == "2":
                    while True:
                        browser = webdriver.Chrome(
                            "./chromedriver/chromedriver.exe")

                        print('step 2')
                        login(browser, email, password)
                        get_stories_geo(browser, geoTag, stories_search, step, email)
                if str(step) == "3":
                    while True:
                        print('step 3')
                        users = get_followees(subTag, users_parse)
                        browser = webdriver.Chrome(
                            "./chromedriver/chromedriver.exe")
                        login(browser, email, password)
                        get_stories_sub(browser, users, step, email)
                        browser.quit()
                        browser.close()

                if str(step) == "4":
                    print('step 4')
                    browser = webdriver.Chrome("./chromedriver/chromedriver.exe")
                    login(browser, email, password)
                    get_users(browser, sub, scroll_analytic, users_parse, email)

                if str(step) == "5":
                    browser = webdriver.Chrome(
                        "./chromedriver/chromedriver.exe")

                    print('step 5')
                    login(browser, email, password)
                    get_on_sub(browser, ingore, email, scroll_on_sub)
                if str(step) == "6":
                    while True:
                        print('step 6')
                        generate_files()
                if str(step) == "7":
                    browser = webdriver.Chrome(
                        "./chromedriver/chromedriver.exe")

                    print('step 7')
                    login(browser, email, password)
                    send_message(browser, message_send,
                                 msg_limit, followes_scroll, step, email)

                elif step == None:
                    ""
            else:
                print(
                    f"В базе не было найдено объекта с шагом {input_step}")

    else:
        print("Функция не обронужена :(")
