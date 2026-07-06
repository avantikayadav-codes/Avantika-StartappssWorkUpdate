from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass

class GoogleLogin(Authentication):

    def login(self):
        print("Google Login Successful")

class EmailLogin(Authentication):

    def login(self):
        print("Email Login Successful")

class FacebookLogin(Authentication):

    def login(self):
        print("Facebook Login Successful")

obj1 = GoogleLogin()
obj2 = EmailLogin()
obj3 = FacebookLogin()

obj1.login()
obj2.login()
obj3.login()