import лаба7.utils.json_service as json_service


def get_id(id):
    db = json_service.get_database()

    for i in db["groups"]:
        if i["id"] == id:
            return i

    return {"message": f"Element with id {id} was not found"}


def get_all():
    db = json_service.get_database()

    return db["groups"]


def enter_group():
    input_str = input("Введите данные группы в формате json: ")
    input_dict = json.loads(input_str)
    return input_dict


def update_id(id, groups):
    db = json_service.get_database()

    for i, elem in enumerate(db["groups"]):
        if elem["id"] == id:
            elem["name"] = groups["name"]
            # elem["contacts"] = users["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Element with {id} was not found"}


def delete_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["groups"]):
        if elem["id"] == id:
            new_group = db["groups"].pop(i)

            json_service.set_database(db)
            return new_group
            # return {"message": f"Group with {id} has been deleted"}

    return {"message": f"Element with {id} was not found"}


def create_group(group):
    db = json_service.get_database()

    last_group_id = get_all()[-1]["id"]
    db["groups"].append({"id": last_group_id + 1, **group})

    json_service.set_database(db)


def joining_user_to_a_group(user_id, group_id):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]):
        for j, el in enumerate(db["groups"]):
            if elem["id"] == user_id and el["id"] == group_id:
                if el["id"] in elem["groups_id"] and elem["id"] in el["users_id"]:
                    json_service.set_database(db)

                    return {"message": f"User with id {user_id} is a subscriber of group with id {group_id}"}

                if el["id"] in elem["groups_id"] and not (elem["id"] in el["users_id"]):
                    # добавляем id пользователя в базу группы
                    el["users_id"].append(user_id)

                    json_service.set_database(db)

                if not (el["id"] in elem["groups_id"]) and elem["id"] in el["users_id"]:
                    el["users_id"].pop(user_id)

                    json_service.set_database(db)
                    return {"message": f"User with id {user_id} is not a subscriber of group with id {group_id}"}

                if not (el["id"] in elem["groups_id"]) and not(elem["id"] in el["users_id"]):
                    return {"message": f"User with id {user_id} is not a subscriber of group with id {group_id}"}

                if el["id"] != group_id:
                    return {"message": f"Element with id {group_id} was not found"}

                if elem["id"] != user_id:
                    return {"message": f"Element with id {user_id} was not found"}


