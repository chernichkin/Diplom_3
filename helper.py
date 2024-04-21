from faker import Faker


def generate_payloads():
    fake = Faker()
    email = fake.email()
    name = fake.name()
    password = "111111"
    payload = {'email': email, 'password': password, 'name': name}
    return payload


def list_compare(list1, list2):
    return all(item in list2 for item in list1)
