import json

def getUserInfo():
    try:
        with open("user_info.json", "r") as file:
            user_info = json.load(file)
            return user_info
    except FileNotFoundError:
        # File not found, prompt user for info and create a new file
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        password = input("Password ")
        user_info = {f'{name}':{'age':age, 'password': password}}

        with open("user_info.json", "w") as file:
            json.dump(user_info, file)

        return user_info
    
if __name__ == '__main__':
    userInfo = getUserInfo()
    print(userInfo)
