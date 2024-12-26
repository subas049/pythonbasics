print("Please enter numbers to add in list and enter z to stop : ")
num_list=[]
while True:
    num=input()
    if num=='z':
        break
    num_list.append(num)
print(num_list)
