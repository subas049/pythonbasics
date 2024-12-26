'''letter=' '

while not letter.isalpha():
    letter=input("Enter an alphabet : ")
print("you have entered : "+letter)

#print numbers 1 to 100
number=0
while number<=100:
    print(number)
    number+=1
print("completed")'''

for i in range(0,100+1,2):
    print(i)
print('bye')

lis=[1,3,5,3,4,5,2,7,8]

for i in lis:
    print(i*5)
else:
    print('for loop completed')
print("completed")

