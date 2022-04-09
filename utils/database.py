import json
import os


def register_user(user_name: str = '', data: dict = None, filepath='users.json'):
    if not os.path.isfile(filepath):
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.write('{}')

    with open(filepath, mode='r', encoding='utf-8') as f:
        old_data = json.load(f)

    with open(filepath, mode='w', encoding='utf-8') as f:
        old_data[user_name] = data
        json.dump(old_data, f, indent=4)


def load_users(filepath='users.json'):
    if not os.path.isfile(filepath):
        return print('[Error]: This file doesn\'t exist.')

    with open(filepath, mode='r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    # Insert a new user:
    register_user('UserNameID1', {'age': 10, 'sock_size': 84, 'shirt_amount': 93})
    register_user('UserNameID2', {'gender': 'M', 'sock_size': 83, 'shirt_amount': 4})

    # Retrieving the users:
    users = load_users()
    print(users['Name'])
    print(users['UserNameID1'])
    print(users['UserNameID2'])