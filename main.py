import лаба7.utils.json_service as json_service
import components.groups.service as group
import components.friends.service as friend
import components.users.service as user
import components.cities.service as city

print("Facebook")


def print_menu():
    print("1. Показать всех пользователей")
    print("2. Показать информацию о пользователе по ID")
    print("3. Создать нового пользователя")
    print("4. Обновить информацию о пользователе по ID")
    print("5. Удалить пользователя по ID")
    print("6. Показать все группы")
    print("7. Показать информацию о группе по ID")
    print("8. Создать новую группу")
    print("9. Обновить информацию о группе по ID")
    print("10. Удалить группу по ID")
    print("11. Присоединить пользователя к группе")
    print("12. Показать всех друзей")
    print("13. Показать информацию о друзьях по ID")
    print("14. Создать группу друзей")
    print("15. Удалить группу друзей по ID")
    print("16. Добавить друзей")
    print("17. Показать все города")
    print("18. Показать информацию о городе по ID")
    print("19. Создать новый город")
    print("20. Обновить информацию о городе по ID")
    print("21. Удалить город по ID")
    print("0. Выйти")


while True:
    print_menu()
    choice = input("Выберите действие (введите номер): ")

    if choice == "0":
        break
    elif choice == "1":
        print(user.get_all())
    elif choice == "2":
        user_id = input("Введите ID пользователя: ")
        print(user.get_id(int(user_id)))
    elif choice == "3":
        print("Введите следующие данные о пользователе: username, gender, birthdate, contacts (email, phone), password, city_id, groups_id, friends_id")
        print(user.create_user(user.enter_user()))
        pass
    elif choice == "4":
        user_id = input("Введите ID пользователя: ")
        print("Введите следующие данные о пользователе: username, contacts (email, phone), password")
        print(user.update_id(int(user_id), user.enter_user()))
        pass
    elif choice == "5":
        user_id = input("Введите ID пользователя для удаления: ")
        print(user.delete_id(int(user_id)))
    elif choice == "6":
        print(group.get_all())
    elif choice == "7":
        group_id = input("Введите ID группы: ")
        print(group.get_id(int(group_id)))
    elif choice == "8":
        print("Введите следующие данные о группе: name, users_id")
        print(group.create_group(group.enter_group()))
        pass
    elif choice == "9":
        group_id = input("Введите ID группы: ")
        print("Введите следующие данные о группе: name")
        print(group.update_id(int(group_id), group.enter_group()))
    elif choice == "10":
        group_id = input("Введите ID группы для удаления: ")
        print(group.delete_id(int(group_id)))
    elif choice == "11":
        user_id = input("Введите ID пользователя: ")
        group_id = input("Введите ID друга: ")
        print(group.joining_user_to_a_group(int(user_id), int(group_id)))
        pass
    elif choice == "12":
        print(friend.get_all())
    elif choice == "13":
        group_of_friends_id = input("Введите ID группы друзей: ")
        print(friend.get_id(int(group_of_friends_id)))
    elif choice == "14":
        print("Введите следующие данные о группе друзей: users_id")
        print(friend.create_group_of_friends(friend.enter_friends()))
        pass
        # попытки сделать вывод ошибки при вводе несуществующих id   
        '''
        db = json_service.get_database()
        for i in db["users"]:
            for p, elem in enumerate(friend.enter_friends()):
                # for k in range(len(friend.enter_friends()[elem])):
                for j in range(len(friend.enter_friends()[elem])):
                    if i["id"] == friend.enter_friends()[elem][j]:
                        print("Element with id", friend.enter_friends()[elem][j], "cannot be added")
                        # print(friend.create_group_of_friends(friend.enter_friends()))

                    # else:
                    # print("Element with id", friend.enter_friends()[elem][k], "cannot be added")

                print(friend.create_group_of_friends(friend.enter_friends()))
        '''
        '''
        value = friend.enter_friends()#["users_id"]
        db = json_service.get_database()
        for i in value["users_id"]:
            for j in db["users"]:
                if i in db["users"]:
                    print(friend.create_group_of_friends(friend.enter_friends()))
                    #print("Element with id", i, "cannot be added")

                print(friend.create_group_of_friends(friend.enter_friends()))
            else:
                print("Element with id", i, "cannot be added")
       '''
        
    elif choice == "15":
        group_id = input("Введите ID группы друзей для удаления: ")
        print(friend.delete_group_of_friends_id(int(group_id)))
    elif choice == "16":
        user_id = input("Введите ID пользователя: ")
        friend_id = input("Введите ID друга: ")

        db = json_service.get_database()
        for i in db["users"]:
            if i["id"] != int(user_id) and int(user_id) >= int(friend_id):
                print("Element with id", user_id, "was not found")
                break
            if i["id"] != int(friend_id):
                print("Element with id", friend_id, "was not found")
                break
            else:
                print(friend.adding_friends(int(user_id), int(friend_id)))
        pass

    elif choice == "17":
        print(city.get_all())
    elif choice == "18":
        city_id = input("Введите ID города: ")
        print(city.get_id(int(city_id)))
    elif choice == "19":
        print("Введите следующие данные о городе: name")
        print(city.create_city(city.enter_city()))
        pass
    elif choice == "20":
        city_id = input("Введите ID города: ")
        print("Введите следующие данные о городе: name")
        print(city.update_id(int(city_id), city.enter_city()))
        pass
    elif choice == "21":
        city_id = input("Введите ID города: ")
        print(city.delete_id(int(city_id)))

    else:
        print("Неверный выбор. Пожалуйста, выберите корректный номер.")
