import json
import os


def generate_files_to_tracker():
    with open(f"./settings/users-settings.json", "r") as f:
        data = json.load(f)

    for u in data:
        link = u["email"]
        path = f"./tracker/{link}.json"
        if os.path.isfile(path) == False:
            with open(f"./tracker/{link}.json", "w") as file:
                file.write("{}")

            data = {
                "step_1":{
                    "likes": 0,
                    "stories": 0,
                    "messages_sended": 0,
                    "in_work": 0
                },

                "step_2":{
                    "likes": 0,
                    "stories": 0,
                    "messages_sended": 0,
                    "in_work": 0
                },

                "step_3":{
                    "likes": 0,
                    "stories": 0,
                    "messages_sended": 0,
                    "in_work": 0
                },
                "step_7":{
                    "likes": 0,
                    "stories": 0,
                    "messages_sended": 0,
                    "in_work": 0
                }
            }

            with open(f"./tracker/{link}.json", "w") as f:
                json.dump(data, f, indent=3)


    print("Файлы успешно созданы")

def delete_files_to_tracker():
    with open(f"./settings/users-settings.json", "r") as f:
        data = json.load(f)

    for u in data:
        link = u["email"]
        
        with open(f"./tracker/{link}.json", "w") as file:
            file.write("{}")

        data = {
            "step_1":{
                "likes": 0,
                "stories": 0,
                "messages_sended": 0,
                "in_work": 0
            },

            "step_2":{
                "likes": 0,
                "stories": 0,
                "messages_sended": 0,
                "in_work": 0
            },

            "step_3":{
                "likes": 0,
                "stories": 0,
                "messages_sended": 0,
                "in_work": 0
            },
            "step_7":{
                "likes": 0,
                "stories": 0,
                "messages_sended": 0,
                "in_work": 0
            }
        }

        with open(f"./tracker/{link}.json", "w") as f:
            json.dump(data, f, indent=3)


    print("Файлы успешно удалены")


def generate_files():
    with open(f"./settings/users-settings.json", "r") as f:
        data = json.load(f)

    for u in data:
        link = u["users_parse"][0]["user_name"]
        with open(f"./analytics/{link}.json", "w") as file:
            file.write(f"[]")

        data = [
                {
                    "commercial": 0,
                    "foreign": 0,
                    "massfollowers": 0,
                    "inactive": 0,
                    "profile_activity": 0,
                    "available_audience": 0,
                    "genuine_audience": 0
                }
        ]
        
        with open(f"./analytics/{link}.json", "w") as f:
            json.dump(data, f, indent=3)
        
            
    print("Файлы успешно созданы")
