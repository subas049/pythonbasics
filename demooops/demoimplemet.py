from User import UserDemo,StudentDemo,TeacherDemo,TempDemo

user1 = UserDemo("Subash", "Perumal")
user2 = UserDemo("Moorthy", "Chidambaram")
user3 = UserDemo("Pirama", "U")

user1.register()
user2.login()
user3.register()
user3.login()

print(user1.user_name)
print(user2.pwd)
print("No of users is : "+ str(UserDemo.users))

student1=StudentDemo("Subash","Perumal","80000","ECE")
student1.greet_student()

teacher1=TeacherDemo("Subash", "Perumal")
teacher1.dept()

student1.login()
teacher1.login()

temp1=TempDemo("Subash", "Perumal")
temp1.login()
temp1.dept()


