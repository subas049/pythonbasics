num=int(input("Type a number from 1 to 20 : "))

div=1
lst=[]

while num>=div:
    if num%div==0:
        lst.append(div)
    div+=1

print(lst)
