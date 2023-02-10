import json
import tabulate


def write_json_data(file, key, value):
    with open(f"./tracker/{file}.json", "r") as f:
        data = json.load(f)

    data.__setitem__(key, value)

    with open(f"./tracker/{file}.json", "w") as f:
        json.dump(data, f, indent=3)


def get_info(step, user, likes, stories, messages_sended, in_work):

    with open(f"./tracker/{user}.json", "r") as f:
        data = json.load(f)

    for key, value in data.items():
        if f'step_{step}' == key:
            write_json_data(user, key, {
                "likes": value["likes"]+likes,
                'stories': value["stories"]+stories, 
                'messages_sended': value["messages_sended"]+messages_sended, 
                'in_work': in_work
            })
    
    with open(f"./tracker/{user}.json", "r") as f:
        data = json.load(f)
    for key, value in data.items():
        if f'step_{step}' == key:
            dict = [["step", "likes", "stories", "messages_sended", "in_work"]]

            dict.append([step, value["likes"], value["stories"], value["messages_sended"], value["in_work"]])
    
    results = tabulate.tabulate(dict)
    print(results)
