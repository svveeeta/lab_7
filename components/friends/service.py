import лаба7.utils.json_service as json_service


def get_id(id):
    db = json_service.get_database()
    for i in db["friends"]:
        if i["id"] == id:
            return i
        return {"message": f"Element with id {id} was not found"}


def get_all():
    db = json_service.get_database()

    return db["friends"]

def enter_friends():
    input_str = input("Введите данные группы друзей в формате json: ")
    input_dict = json.loads(input_str)
    return input_dict

def delete_group_of_friends_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["friends"]):
        if elem["id"] == id:
            new_group = db["friends"].pop(i)

            json_service.set_database(db)
            return new_group
            # return {"message": f"Group with {id} has been deleted"}

    return {"message": f"Element with id {id} was not found"}


def create_group_of_friends(group):
    db = json_service.get_database()

    last_group_id = get_all()[-1]["id"]
    db["friends"].append({"id": last_group_id + 1, **group})

    json_service.set_database(db)


def adding_friends(user_id, friend_id):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]):
        for j, el in enumerate(db["users"]):
            if elem["id"] == user_id and el["id"] == friend_id:
                if elem["id"] in el["friends_id"] and el["id"] in elem["friends_id"]:
                    json_service.set_database(db)

                    return {"message": f"User with id {user_id} is a friend of user with id {friend_id}"}

                if elem["id"] in el["friends_id"] and not (el["id"] in elem["friends_id"]):
                    elem["friends_id"].append(user_id)

                    json_service.set_database(db)

                    for k, element in enumerate(db["friends"]):
                        # добавляем id пользователей в базу друзей
                        if not (elem["id"] in element["users_id"]) or not (el["id"] in element["users_id"]):
                            element["users_id"].append(user_id)

                            json_service.set_database(db)
                            return element["users_id"]


                if not (elem["id"] in el["friends_id"]) and el["id"] in elem["friends_id"]:
                    el["friends_id"].append(friend_id)

                    json_service.set_database(db)

                    for k, element in enumerate(db["friends"]):
                        # добавляем id пользователей в базу друзей
                        if not (elem["id"] in element["users_id"]) or not (el["id"] in element["users_id"]):
                            element["users_id"].append(user_id)

                            json_service.set_database(db)
                            return element["users_id"]

                        if (elem["id"] in element["users_id"] and not (elem["id"] in el["friends_id"])) or (
                                elem["id"] in element["users_id"] and not (el["id" in elem["friends_id"]])):
                            element["users_id"].pop(elem["id"])
                            element["users_id"].pop(el["id"])

                            json_service.set_database(db)
                            return element["users_id"]


                else:
                    #json_service.set_database(db)
                    return {"message": f"User with id {user_id} is not a friend of user with id {friend_id}"}

        if elem["id"] != user_id:
            return {"message": f"Element with id {user_id} was not found"}

        if friend_id != elem["id"]:
            return {"message": f"Element with id {friend_id} was not found"}

