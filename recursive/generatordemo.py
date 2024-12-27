squgen=[]
def sqrnum(num):
    for i in range(num+1):
        squgen.append(i*i)
    return squgen

def squ_generator(number):
    for i in range(number+1):
        yield i*i


print(sqrnum(10))
for i in squ_generator(10):
    print(i)
