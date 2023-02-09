import json

def get_user_settings():
    with open(f"./settings/users-settings.json", "r") as f:
        data = json.load(f)
    return data

def get_user_analytics():
    with open(f"./storage/users_analytics.json", "r") as f:
        data = json.load(f)
    return data

        