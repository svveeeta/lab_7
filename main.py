import components.groups.service as group
import components.friends.service as friend
import components.users.service as user
import components.cities.service as city

# USERS
#print(user.get_all())

#print(user.get_id(1))

s=

print(user.create_user({
       "username": "Test Test",
        "gender": "female",
        "birthdate": "01.01.1111",
        "contacts": {
            "phone": "+11111111",
            "email": "test@gmail.com"
        },
        "password": "t1t1t1",
        "city_id": 1,
        "groups_id": [
            1
        ],
        "friends_id": [
            1000
        ]
    }))

'''
print(user.update_id(6, {
    "username": "SOMEBODY",
    "contacts": {
        "phone": "+90909090",
        "email": "sb@gmail.com"
    },
    "password": "xrxrxr"
    }))
'''
#print(user.delete_id(6))


# GROUPS
#print(group.get_all())

#print(group.get_id(2))
'''
print(group.create_group({
        "name": "test",
        "users_id": [
            1
        ]
    }))
'''
''''
print(group.update_id(6,{
        "name": "TEST"
    }))
'''
#print(group.delete_id((6)))

#print(group.joining_user_to_a_group(1,2))


#FRIENDS
#print(friend.get_all())
#print(friend.get_id(5))
'''
print(friend.create_group_of_friends({
        "users_id": [
            1,
            2,
            3
        ]
    }))
'''
#print(friend.delete_group_of_friends_id(4))

#print(friend.adding_friends(1, 4))


# CITIES
'''
print(city.get_all())
print(city.get_id(1))

print(city.create_city({
    "name": "Test"
}))

print(city.update_id(4, {
    "name": "Los Angeles"
}))

print(city.delete_id(4))
'''





