from faker import Faker

fake = Faker()

headers = {
    "Content-Type": "application/json"
}

order_body = {
    "firstName": fake.first_name(),
    "lastName": "Фамилия",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 25,
    "phone": "+34916123451",
    "rentTime": 5,
    "deliveryDate": "2024-10-15",
    "comment": "Привет, Абдурахмангаджи!",
    "color": [
        "BLACK"
    ]
}