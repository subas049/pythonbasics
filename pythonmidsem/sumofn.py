def sumofnnumbers(n):
    if n<=1:
        return n
    elif n>=2:
        return n+sumofnnumbers(n-1)


n=int(input("Please enter a number to find its sum : "))
print(sumofnnumbers(n))




