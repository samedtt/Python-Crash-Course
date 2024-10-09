class Users:

    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, your age is {self.age} and gender is {self.gender}.")

class Privileges:
    def __init__(self,privileges):
        self.privileges=privileges

    def show_privileges(self):
        print("Administor's set of privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")    

class Admin(Users):
    def __init__(self,first_name,last_name,age,gender,privileges):
        super().__init__(first_name,last_name,age,gender)
        self.privileges=Privileges(privileges)