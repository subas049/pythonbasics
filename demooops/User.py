class UserDemo:
    users = 0  # class variable

    def __init__(self, user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd
        UserDemo.users += 1  # Increment class variable

    def register(self):
        print("Registering... " + self.user_name)

    def login(self):
        print("Logging in ... " + self.user_name)


class StudentDemo(UserDemo):  # inheriting user demo class
    def __init__(self, user_name, pwd, fee, dept):
        super().__init__(user_name,pwd)
        self.fee = fee
        self.dept = dept

    def greet_student(self):
        print(f"Hi Welcome {self.user_name} ! ")
        print(f"Hi  {self.pwd} ! ")
        print(f"Hi your fee is {self.fee} ! ")
        print(f"Hi your dept is {self.dept} ! ")
        super().register()


class TeacherDemo(UserDemo):  # inheriting user demo class
    def dept(self):
        print("Hi this is from ECE dept")


class TempDemo(TeacherDemo):  # inheriting teacherdemo class
    def sample(self):
        print("Hi this is from temp faculty from ECE dept")
