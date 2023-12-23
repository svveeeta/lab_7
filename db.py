db = {
    "social media": "Facebook",
    "users": [
        {
            "id": 1,
            "username": "Timothee Chalamet",
            "gender": "male",
            "birthdate": "27.12.1995",
            "contacts": {
                "phone": "+12980785",
                "email": "chalamet@gmail.com"
            },
            "password": "x1x1x1",
            "city_id": 1,
            "groups_id": [
                1,
                4
            ],
            "friends_id": [
                2,
                4
            ]
        },
        {
            "id": 2,
            "username": "Shawn Mendes",
            "gender": "male",
            "birthdate": "08.08.1998",
            "contacts": {
                "phone": "+14782340",
                "email": "shawn@gmail.com"
            },
            "password": "y1y4y1",
            "city_id": 2,
            "groups_id": [
                2,
                4,
                5
            ],
            "friends_id": [
                1
            ]
        },
        {
            "id": 3,
            "username": "Virginia Miller",
            "gender": "female",
            "birthdate": "07.11.2005",
            "contacts": {
                "phone": "+14367805",
                "email": "ginny@gmail.com"
            },
            "password": "h0h0h0",
            "city_id": 3,
            "groups_id": [
                3,
                5
            ],
            "friends_id": [
                5
            ]
        },
        {
            "id": 4,
            "username": "Saoirse Una Ronan",
            "gender": "female",
            "birthdate": "12.06.1994",
            "contacts": {
                "phone": "+18734679",
                "email": "saoirse@gmail.com"
            },
            "password": "67gh67",
            "city_id": 1,
            "groups_id": [
                1,
                3,
                5
            ],
            "friends_id": [
                1
            ]
        },
        {
            "id": 5,
            "username": "Kanye West",
            "gender": "female",
            "birthdate": "08.06.1977",
            "contacts": {
                "phone": "+13343276",
                "email": "kanye@gmail.com"
            },
            "password": "w0w0ww",
            "city_id": 3,
            "groups_id": [
                2,
                4
            ],
            "friends_id": [
                3
            ]
        }
    ],
    "cities": [
        {
            "id": 1,
            "name": "New York",
            "users_id": [
                1,
                4
            ]
        },
        {
            "id": 2,
            "name": "Toronto",
            "users_id": [
                2
            ]
        },
        {
            "id": 3,
            "name": "Atlanta",
            "users_id": [
                3,
                5
            ]
        }
    ],
    "friends": [
        {
            "id": 1,
            "users_id": [
                1,
                4
            ]
        },
        {
            "id": 2,
            "users_id": [
                3,
                5
            ]
        },
        {
            "id": 3,
            "users_id": [
                1,
                2
            ]
        }
    ],
    "groups": [
        {
            "id": 1,
            "name": "cinematography",
            "users_id": [
                1,
                4
            ]
        },
        {
            "id": 2,
            "name": "music",
            "users_id": [
                2,
                5
            ]
        },
        {
            "id": 3,
            "name": "poetry",
            "users_id": [
                3,
                4
            ]
        },
        {
            "id": 4,
            "name": "fashion",
            "users_id": [
                1,
                2,
                5
            ]
        },
        {
            "id": 5,
            "name": "psychology",
            "users_id": [
                2,
                3,
                4
            ]
        }
    ]
}