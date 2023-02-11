from langdetect import detect
import instaloader
from instaloader.structures import Profile
import json
from instaloader.exceptions import BadCredentialsException, ConnectionException, ProfileNotExistsException
from langdetect.lang_detect_exception import LangDetectException
from datetime import datetime, date
from generate_files import generate_files
from itertools import groupby

def save_info(path, obj):
    with open(f"./storage/users_analytics.json", "r") as f:
        data = json.load(f)

    data.append(obj)

    with open(f"./storage/users_analytics.json", "w") as f:
        json.dump(data, f, indent=3)


def get_followees(sub, user, passwd):
    for s in sub:
        print(user, passwd)
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
            for user_ in profile.get_followers():
                try:
                    use__ = Profile.from_id(l.context, user_.followees).username
                    print(use__)
                    users.append(use__)
                except ProfileNotExistsException:
                    print("Аккаунт не был записан так как он заблокировал вас")
                    continue
        except ConnectionException:
            print(f"Аккаунт {user} времено в блокировке")
            continue

        new_hrefs = [el for el, _ in groupby(users)]
        print(new_hrefs)
        l.close()
        return new_hrefs
        

def get_analytics(sub, user, passwd):
    generate_files()
    for s in sub:
        print(user, passwd)
        path = f'./sessions/{user}.'
        l = instaloader.Instaloader(compress_json=False)

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
            for user_ in profile.get_followers():

                user_name = user_.username
                is_business_account = user_.is_business_account
                followers = user_.followers
                followees = user_.followees  # Sub
                biography = user_.biography
                img = user_.profile_pic_url
                id_ = user_.userid
                sub_profile = Profile.from_username(l.context, user_name)
                # me_profile = Post(l.context, )

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

                for posts in sub_profile.get_posts():
                    posts_counter = 0
                    post_date = str(posts.date_local)

                    a = post_date.split(" ")[0].split("-")
                    b = str(datetime.now().date()).split("-")

                    print(a, b)
                    aa = date(int(a[0]), int(a[1]), int(a[2]))
                    bb = date(int(b[0]), int(b[1]), int(b[2]))
                    cc = str(bb-aa).split(",")[0]

                    if cc > "89":
                        user_info[0]["active"] = "last post 3 months ago"
                        print("HERE 1")
                    else:
                        user_info[0]["active"] = f"last post date {a}"
                        print("HERE 2")

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

                print(user_info)

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

                try:
                    with open(f"./analytics/{user}.json", "w") as f:
                        json.dump(data, f, indent=3)
                except FileNotFoundError:
                    print("Запустите шаг 6 прежде чем запускать аналитику !!!")
                    continue

        except ConnectionException:
            print(f"Аккаунт {user} времено в блокировке")
            continue
        except ProfileNotExistsException:
            print("Аккаунт не был записан так как он заблокировал вас")
            continue

        l.close()
