from functions import select_function
from utils.analytics_functions.get_analytics import get_analytics


get_analytics(["sreda.app"], [
        {
            "user_name": "marina.vinogradova5740",
            "user_password": "U4fOiIt4jG"
        },
        {
            "user_name": "darja.martynova6575",
            "user_password": "I8bOiOm8fF"
        }], "sreda.app")

# try:
#     select_function()
# except KeyboardInterrupt:
#     print("Процесс был остоновлен в ручную админом")

# users_parse = ["user1","user2","user3","user4","user5","user6","user7","user8","user10","user11","user12","user13","user14","user15","user16","user17","user18",]
# users_login = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# i_min = 0
# i_max = i_min+1
# for parse in users_parse:
#     for user in users_login:
#         print(f"user:{user}", f"parse:{parse}")
#         users_login.remove(user)
#         break
