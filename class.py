import uuid

class User:
    all, all_usernames, all_ids = [], [], []

    @classmethod
    def signup(cls):
        

    def __init__(self, username: str, password: str, phone_number: str = None):
        self.username, self.__password = username, password
        self.phone_number = phone_number
        self.user_id = User.uuid_gen(username)
        User.all.append(self)
        User.all_ids.append(self.user_id)
        User.all_usernames.append(username)
    
    @staticmethod
    def uuid_gen(name):
        x = uuid.uuid1()
        return uuid.uuid5(x, name)


    @staticmethod
    def username_check(usr_nm):
        if usr_nm in User.all_usernames:
            return False
        return True

    @property
    def username(self):
        if self.username not in User.all_usernames:
            return self.username
    
    @username.setter
    def username(self, user_value):
        if not User.username_check(user_value):
            raise ValueError("Username is already taken! ")
        

    @staticmethod
    def password_check(passwd):
        if len(passwd) < 4:
            return False
        return True

    @property
    def __password(self):
        return self.__password
    
    @__password.setter
    def __password(self, passwd_value):
        if not User.password_check(passwd_value):
            raise ValueError("Too short Password! ")


user1 = User("Matin", "matinghane", phone_number="09197951537")
user2 = User("Saman", "SamanZarrin")
user3 = User("Mehdi", "driving", phone_number="09365181897")

print(User.all)
print(User.all_usernames)
print(User.all_ids)
