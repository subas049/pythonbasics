# Recursion is a function is calling itself

def nfact(n):
    if n==0:
        return 1
    return n*nfact(n-1)

print(nfact(5))

n1=0
n2=1
count=1
def febinosi(number):
    global n1
    global n2
    global count
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    while count<=number:
        count+=1
        febinosi(number)


print(febinosi(5))
