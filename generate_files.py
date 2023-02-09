import json

def generate_files():
    with open(f"./settings/users-settings.json", "r") as f:
        data = json.load(f)

    for u in data:
        link = u["email"]
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
