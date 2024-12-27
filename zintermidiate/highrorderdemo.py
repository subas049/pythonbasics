def happy():
    print("Im happy, thanks")

def sad():
    print("Im sad but no issues, thanks")

happy()
sad()
print(happy)
joy=happy
joy()

sorrow=sad
sorrow()
sad()

def feeling(func): # higher order function
    func()

feeling(sad)
feeling(happy)
