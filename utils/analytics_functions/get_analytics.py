from langdetect import detect
import instaloader
from instaloader.structures import Profile
import json
from instaloader.exceptions import LoginRequiredException, BadCredentialsException, ConnectionException, ProfileNotExistsException, QueryReturnedBadRequestException
from instaloader.exceptions import TooManyRequestsException
from langdetect.lang_detect_exception import LangDetectException
from datetime import datetime, date
from itertools import groupby
import time

def save_info(path, obj):
    with open(f"./storage/{path}.json", "r") as f:
        data = json.load(f)

    data.append(obj)

    with open(f"./storage/{path}.json", "w") as f:
        json.dump(data, f, indent=3)


def get_followees(sub, users_parse):

    user = users_parse[0]["user_name"]
    passwd = users_parse[0]['user_password']
    print(user, passwd)
    session_path = f'./sessions/{user}.'
    l = instaloader.Instaloader(compress_json=False)
    users = []

    try:
        l.load_session_from_file(user, session_path)
    except FileNotFoundError:
        try:
            l.login(user, passwd)
            l.save_session_to_file(session_path)
        except ConnectionException:
            print(f"Аккаунт {user} времено в блокировке")
        except BadCredentialsException:
            print("Пароль не верный")

    except ConnectionException:
        print(f"Аккаунт {user} времено в блокировке")

    for s in sub:
        try:
            profile = Profile.from_username(l.context, s)
            for followes_ in profile.get_followers():
                time.sleep(20)
                users.append(followes_.username)
                print(followes_.username)


        except ConnectionException:
            print(f"Аккаунт {user} времено в блокировке")
            break
        except QueryReturnedBadRequestException:
            print(f"Похоже что аккаунт {user} временно заблокировали")
            break

        new_hrefs = [el for el, _ in groupby(users)]
        l.close()
        return new_hrefs


def get_analytics(subs, users, email):
    i = 0
    max_req = 1
    step = 0
    current_user = [users[0]]
    all_parsed = 0
    for s in subs:
        for u in current_user:
            if i < max_req:
                user = u["user_name"]
                passwd = u['user_password']
                session_path = f'./sessions/{user}.'
                user_analytic_path = f"./analytics/{email}.json"
                print(f'\n{user, passwd}\n')

                l = instaloader.Instaloader(compress_json=False)

                try:
                    l.load_session_from_file(user, session_path)
                except FileNotFoundError:
                    try:
                        l.login(user, passwd)
                        l.save_session_to_file(session_path)
                    except ConnectionException:
                        print(f"Аккаунт {user} времено в блокировке")
                        i = max_req
                        break
                    except BadCredentialsException:
                        print("Пароль не верный")
                        i = max_req
                        break

                except ConnectionException:
                    print(f"Аккаунт {user} времено в блокировке")
                    i = max_req
                    break

                try:
                    time.sleep(5)
                    profile = Profile.from_username(l.context, s)
                    user_name = profile.username
                    is_business_account = profile.is_business_account
                    followers = profile.followers
                    followees = profile.followees
                    biography = profile.biography
                    img = profile.profile_pic_url

                    user_info = [{
                        "user": user_name,
                        "business": False,
                        "language": False,
                        "massfollowers": False,
                        "available_audience": False,
                        "active": "last post 3 months ago",
                        "profile_activity": False,
                        "genuine_audience": False
                    }]


                    for posts in profile.get_posts():
                        posts_counter = 0
                        post_date = str(posts.date_local)

                        a = post_date.split(" ")[0].split("-")
                        b = str(datetime.now().date()).split("-")

                        aa = date(int(a[0]), int(a[1]), int(a[2]))
                        bb = date(int(b[0]), int(b[1]), int(b[2]))
                        cc = str(bb-aa).split(",")[0]

                        if cc > "89":
                            user_info[0]["active"] = "last post 3 months ago"
                        else:
                            user_info[0]["active"] = f"last post date {a}"

                        if posts_counter == 0:
                            break
                        posts_counter += 1

                    try:
                        country = detect(biography)
                    except LangDetectException:
                        country = "ru"

                    if followers > 1499:
                        user_info[0]["massfollowers"] = True

                    if followees < 999:
                        user_info[0]["available_audience"] = True

                    if country != "ru":
                        user_info[0]["language"] = True

                    elif country == None:
                        user_info[0]["language"] = None

                    if is_business_account:
                        user_info[0]["business"] = True

                    if img != None:
                        user_info[0]["genuine_audience"] = True

                    print(f"\n{user_info}\n")

                    try:
                        save_info(email, user_info[0])
                    except FileNotFoundError:
                        print("1")
                        print("Запустите шаг 6 прежде чем запускать аналитику !!!")
                        break

                    try:
                        with open(user_analytic_path, "r") as f:
                            data = json.load(f)

                        if user_info[0]["business"]:
                            data[0]["commercial"] += 1

                        if user_info[0]["language"]:
                            data[0]["foreign"] += 1

                        if user_info[0]["massfollowers"]:
                            data[0]["massfollowers"] += 1

                        if user_info[0]["available_audience"]:
                            data[0]["available_audience"] += 1

                        if user_info[0]["genuine_audience"]:
                            data[0]["genuine_audience"] += 1

                        if user_info[0]["profile_activity"]:
                            data[0]["profile_activity"] += 1

                        if user_info[0]["active"] != "last post 3 months ago":
                            data[0]["inactive"] += 1

                        with open(user_analytic_path, "w") as f:
                            json.dump(data, f, indent=3)

                    except FileNotFoundError:
                        print("4")
                        print("Запустите шаг 6 прежде чем запускать аналитику !!!")
                        break

                    i += 1
                    all_parsed += 1
                    print(f"Всего собранно {all_parsed}")
                except QueryReturnedBadRequestException:
                    print(f"Похоже что аккаунт {user} временно заблокировали")
                    break
                except ProfileNotExistsException:
                    print("Удалёный аккаунт")
                    i = max_req
                    break
                except ConnectionException:
                    print(f"Аккаунт {user} времено в блокировке")
                    i = max_req
                    break
                except LoginRequiredException:
                    print("Пользователь не был авторизован")
                    i = max_req
                    break

            else:
                if len(users)-1 == step:
                    step = 0
                else:
                    step += 1

                i=0
                current_user.pop(0)
                current_user.append(users[step])
                break