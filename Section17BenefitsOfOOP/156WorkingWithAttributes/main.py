class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "Paul")
user_2 = User("002", "Jack")

print(user_1.followers)