import лаба7.utils.json_service as json_service

def get_id(id):
    db = json_service.get_database()
    for i in db["cities"]:
        if i["id"] == id:
            return i
        return {"message": f"Element with id {id} was not found"}


def get_all():
    db = json_service.get_database()

    return db["cities"]


def update_id(id, city):
    db = json_service.get_database()

    for i, elem in enumerate(db["cities"]):
        if elem["id"] == id:
            elem["name"] = city["name"]

            json_service.set_database(db)
            return elem

    return {"message": f"Element with id {id} was not found"}


def delete_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["cities"]):
        if elem["id"] == id:
            new_city = db["cities"].pop(i)

            json_service.set_database(db)
            return new_city
            # return {"message": f"Group with {id} has been deleted"}

    return {"message": f"Element with id {id} was not found"}


def create_city(city):
    db = json_service.get_database()

    last_city_id = get_all()[-1]["id"]
    db["cities"].append({"id": last_city_id + 1, **city})

    json_service.set_database(db)
    return {"message": f"New city was created"}




