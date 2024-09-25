import random

from faker import Faker


def create_users(total):
    fake = Faker()
    Faker.seed(1)

    ids = list(range(total))
    random.seed(1)
    random.shuffle(ids)

    elements = [
        {
            "id": ids[i] + 1,
            "email": fake.free_email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.user_name(),
        }
        for i in range(total)
    ]

    return elements
