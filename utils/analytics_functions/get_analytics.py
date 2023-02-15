from langdetect import detect
import instaloader
from instaloader.structures import Profile
import json
from instaloader.exceptions import BadCredentialsException, ConnectionException, ProfileNotExistsException, QueryReturnedBadRequestException, TooManyRequestsException
from langdetect.lang_detect_exception import LangDetectException
from datetime import datetime, date
from generate_files import generate_files
from itertools import groupby
import time

def save_info(path, obj):
    with open(f"./storage/users_analytics.json", "r") as f:
        data = json.load(f)

    data.append(obj)

    with open(f"./storage/users_analytics.json", "w") as f:
        json.dump(data, f, indent=3)


def get_followees(sub, users_parse):
    for s in sub:
        for us in users_parse:
            user = us["user_name"]
            passwd = us['user_password']
            print(user, passwd, s)
            path = f'./sessions/{user}.'
            l = instaloader.Instaloader(compress_json=False)
            users = []

            try:
                l.load_session_from_file(user, path)
            except FileNotFoundError:
                try:
                    l.login(user, passwd)
                    l.save_session_to_file(path)
                except ConnectionException:
                    print(f"Аккаунт {user} времено в блокировке")
                    continue
                except BadCredentialsException:
                    print("Пароль не верный")
                    continue

            try:
                profile = Profile.from_username(l.context, s)
                for followes_ in profile.get_followers():
                    users.append(followes_.username)
                    time.sleep(0.2)
                    print(followes_.username)
            except TooManyRequestsException:
                print(f"Слишком много запросов меняем аккаунт {user}")
                continue
            except ConnectionException:
                print(f"Аккаунт {user} времено в блокировке")
                continue
            except QueryReturnedBadRequestException:
                print(f"Похоже что аккаунт {user} временно заблокировали")
                break
            
            new_hrefs = [el for el, _ in groupby(users)]
            print(new_hrefs)
            l.close()
            return new_hrefs



def get_analytics(subs, users):
    generate_files()
    for s in subs:
        for us in users:
            user = us["user_name"]
            passwd = us['user_password']
            print(f'\n{user, passwd}\nuser:{s}\n')
            path = f'./sessions/{user}.'
            l = instaloader.Instaloader(compress_json=False)
            i = 0

            proxies = {
                'http': 'socks5://pproxy.site:12006',
                'https': 'socks5://pproxy.site:12006'
            }

            try:
                l.load_session_from_file(user, path)
                l.context._session.proxies = proxies
            except FileNotFoundError:
                try:
                    l.login(user, passwd)
                    l.save_session_to_file(path)
                    l.context._session.proxies = proxies

                except ConnectionException:
                    print(f"Аккаунт {user} времено в блокировке")
                    continue
                except BadCredentialsException:
                    print("Пароль не верный")
                    continue

            try:

                    time.sleep(0.3)
                    try:
                        profile = Profile.from_username(l.context, s)
                    except QueryReturnedBadRequestException:
                        print(f"Похоже что аккаунт {user} временно заблокировали")
                        break
                    except ProfileNotExistsException:
                        print("Удалёный аккаунт")
                        break

                    user_name = profile.username
                    is_business_account = profile.is_business_account
                    followers = profile.followers
                    followees = profile.followees  # Sub
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
                        save_info("./storage/users_analytics.json", user_info[0])
                    except FileNotFoundError:
                        print("Запустите шаг 6 прежде чем запускать аналитику !!!")
                        continue

                    try:
                        with open(f"./analytics/{user}.json", "r") as f:
                            data = json.load(f)
                    except FileNotFoundError:
                        print("Запустите шаг 6 прежде чем запускать аналитику !!!")
                        continue

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

                    i+=1
                    print(i)

                    try:
                        with open(f"./analytics/{user}.json", "w") as f:
                            json.dump(data, f, indent=3)
                            break
                    except FileNotFoundError:
                        print("Запустите шаг 6 прежде чем запускать аналитику !!!")
                        continue

            except TooManyRequestsException:
                print(f"Слишком много запросов меняем аккаунт {user}")
                continue
            except ConnectionException:
                print(f"Аккаунт {user} времено в блокировке")
                continue

            l.close()

