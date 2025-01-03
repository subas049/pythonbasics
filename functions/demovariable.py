num=10
name='Subash'
x=10

def printnum(num):
    global x
    x=20
    print('the parameter value is : '+str(num))
    print('the global num value is : '+str(globals()['num']))
    print(str(x))
    print(name)

printnum(50)


while x<=100:
    print(x)
    x+=10
print('completed')

#sum of numbers

def total(*args):
    total=0
    for i in args:
        total =total+i
    return total

print(total(2,3,4,5))
print(total(2,3,4,5,3,4,4,5))

def printaddress(**kwargs):
    for key,val in kwargs.items():
        print(val)

print(printaddress(doorno='No : 93',street='Ashok nagar',Avenue='12th Avenue',city='Chennai'))
