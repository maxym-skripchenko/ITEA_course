lists = ["Max", "Yurii"]

def has_permition(page):
    username = input("Enter your username: ")
    def inner(username):
        for i in lists:
            if username == i:
                return print("Permition given")
            else:
                return print("Invalid user")
    return inner

has_permition(14)