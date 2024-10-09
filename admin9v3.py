from admin9v2 import Users

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