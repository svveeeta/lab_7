import лаба7.utils.json_service as json_service

for i in

def get_id(id):
    db = json_service.get_database()
    for i in db["users"]:
        if i["id"] == id:
            return i
        return {"message": f"Element with id {id} was not found"}


def get_all():
    db = json_service.get_database()

    return db["users"]


def enter_user():
    input_str = input("Введите данные пользователя в формате json: ")
    input_dict = json.loads(input_str)
    return input_dict


def update_id(id, user):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]):
        if elem["id"] == id:
            elem["username"] = user["username"]
            elem["contacts"] = user["contacts"]
            elem["password"] = user["password"]

            json_service.set_database(db)
            return elem

    return {"message": f"Element with id {id} was not found"}


def delete_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]):
        if elem["id"] == id:
            new_user = db["users"].pop(i)

            json_service.set_database(db)
            return new_user
            # return {"message": f"User with id {id} has deleted"}

    return {"message": f"Element with id {id} was not found"}


def create_user(user):
    db = json_service.get_database()

    last_user_id = get_all()[-1]["id"]
    db["users"].append({"id": last_user_id + 1, **user})

    json_service.set_database(db)
    return {"message": f"New user was created"}






