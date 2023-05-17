#! /usr/bin/python3

import uuid


class ShortPasswordError(Exception):
    """
    I use this error when short password Entered
    """


class PasswordError(Exception):
    """
    I use this when wrong password has been Entered
    """


class UserError(Exception):
    """
    I use this error when wrong username Entered
    """


class RepUserError(Exception):
    """
    I use this error when a repeatitious Username has been entered
    """


class TwoPasswordError(Exception):
    """
    I use this error when two new passwords are not match
    """


class User:
    """
    This class is use for modeling users and some functionality/
    like username, password, a unique identifier and phone number./
    this class recieves informations from user and processing them./
    password must longer than 4 characters/
    username must be unique and repetitious usernames not accepted/
    also user can enter his/her phone number and if phone number not entered,
     it assuming to None
    """

    all_users, all_usernames, all_ids = [], [], []

    def __init__(self, username: str, password: str, phone_number: str = None):
        """
        The __init__ method for assigning attributes
        """
        self.username, self.password = username, password
        self.phone_number = phone_number
        self.user_id = User.uuid_gen(username)
        User.all_users.append(self)
        User.all_usernames.append(username)
        User.all_ids.append(self.user_id)

    def __str__(self):
        return f"\n_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\nUser informations: \n\tUsername: {self.username}\n\tPhone number: {self.phone_number}\n\tUser ID: {self.user_id}\n_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\n"

    def sign_in_check(self, user_name, passwd):
        if (user_name == self.username) and (passwd == self.password):
            print("Signing in Completed! ")
        else:
            raise PasswordError("Wrong Password! ")

    @classmethod
    def sign_in_validation(cls, user_name, passwd):
        if user_name not in cls.all_usernames:
            raise UserError("Username not found! ")
        for usr in cls.all_usernames:
            if user_name == usr:
                cls_obj = cls.dictionary[user_name]
        cls_obj.sign_in_check(user_name, passwd)

    dictionary = {}

    @classmethod
    def signup(cls, user_name, passwd, ph_numb):
        """
        This function is for Signing up users.
        first user must enter username, then enter password
        and finally enter phone number
        """
        obj = cls(user_name, passwd, ph_numb)
        User.dictionary[user_name] = obj
        print("\nSignup Completed! ")

    def representation(self):
        print(self)

    @staticmethod
    def username_check(user_name: str) -> bool:
        """
        This static method actually for checking repetitious usernames
        """
        if user_name in User.all_usernames:
            return False
        return True

    def edit_user(self, original_username, usr_name=None, ph_numb=None):
        if usr_name in User.all_usernames:
            raise RepUserError("Username Already taken! ")
        if usr_name is not None:
            self.username = usr_name
        if ph_numb is not None:
            self.phone_number = ph_numb

    def passwd_change(self, old_pass, new_pass, repeat_new_pass):
        if (old_pass != self.password) or (new_pass != repeat_new_pass):
            raise TwoPasswordError("Invalid old Password or not match new passwords")
        self.password = new_pass

    @property
    def username(self):
        """
        Getter for Username
        """
        return self._username

    @username.setter
    def username(self, user_value):
        if not User.username_check(user_value):
            raise RepUserError("Username is already taken! ")
        self._username = user_value

    @staticmethod
    def password_check(passwd):
        """
        This function actually check the password and if its length smaller
        than 4, an ValueError raised with the too short massage
        """
        if len(passwd) < 4:
            return False
        return True

    @property
    def password(self):
        """
        Getter for password
        """
        return self.__password

    @password.setter
    def password(self, passwd_value):
        if not User.password_check(passwd_value):
            raise ShortPasswordError("Too short Password! ")
        self.__password = passwd_value

    @staticmethod
    def uuid_gen(name):
        """
        This function generate a universal unique identifier with uuid5
        and use MD5 Hash algorithm
        """
        x_uuid = uuid.uuid1()
        return uuid.uuid5(x_uuid, name)


def main():
    """
    This is main function of our module
    """
    user1 = User("Matin", "12345678", phone_number="09197951537")
    user2 = User("Saman", "qwerty")
    user3 = User("Matin", "zxcvbnm")
    print(user1.username, user2.username, user3.username, sep="****")
    print(User.all_users)
    print(User.all_usernames)
    print(User.all_ids)


if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#! /usr/bin/python3

from users import (
    User,
    UserError,
    PasswordError,
    TwoPasswordError,
    ShortPasswordError,
    RepUserError,
)


while 1:
    print("\n********** - Welcome to user management panel - **********\n")
    try:
        stat = input("stat (0(Exit) - 1(Sign up) - 2(Log in)):   ")
    except NameError:
        print("\nInvalid State! ")
        continue

    if stat == "0":
        print("\nExiting the User management panel...")
        break

    elif stat == "1":
        print("\n********** ^ Sign up form ^ **********\n")
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            phone_number = input("Enter Phone number(Optional): ")
            User.signup(username, password, phone_number)
        except UserError:
            print("Username already taken! ")
        except ShortPasswordError:
            print("Too short Password! ")

    elif stat == "2":
        print("\n************** - Login form - **************\n")
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            User.sign_in_validation(username, password)
            user_object = User.dictionary[username]
        except UserError:
            print("Username not found! ")
        except PasswordError:
            print("Wrong Password! ")

        while 1:
            print("\n************** - User Dashboard - **************\n")
            stat = int(
                input(
                    "stat (1(show user information) - 2(Edit) - 3(Password change) - 4(Back to main menu))   "
                )
            )

            if stat == "1":
                user_object.representation()

            elif stat == "2":
                print("\n********** ^ Edit User information mode ^ **********\n")
                print(
                    "if you dont want to change any item, just leave it and press Enter.\n"
                )
                try:
                    new_username = input("Enter new Username: ")
                    new_phone_number = input("Enter new phone number: ")
                    user_object.edit_user(username, new_username, new_phone_number)
                except RepUserError:
                    print("Username already taken! ")
                print("\nUser Information has been Updated! ")

            elif stat == "3":
                print("\n********** ^ Password Change ^ **********\n")
                try:
                    old_pass = input("Enter Old Password: ")
                    new_pass = input("Enter New Password: ")
                    rep_new_pass = input("Enter New Password again: ")
                    user_object.passwd_change(old_pass, new_pass, rep_new_pass)
                except ShortPasswordError:
                    print("Too short password! ")
                except TwoPasswordError:
                    print("Two new passwords are not matched! ")
                print("\nYour Password has been changed! ")

            elif stat == "4":
                print("\nExiting User Panel...")
                break
            else:
                print("\nInvalid State! ")
                continue
    else:
        print("\nInvalid State! ")
        continue
