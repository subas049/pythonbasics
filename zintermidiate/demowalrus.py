# name = "Subash"
# print(name)

# Using walrus operator(:=)
print(name:="Subash")

# print("Enter the numbers to add in list and enter 'Z' to exit : ")
# num_list=[]
# while True:
#     ip=input()
#     if ip =='z':
#         break
#     num_list.append(ip)
# else:
#     print("done")
# print(num_list)


# Using walrus operator(:=)
print("Enter the numbers to add in list and enter 'Z' to exit : ")
list_num=list()
while (inp:=input())!='z':
    list_num.append(inp)
print(list_num)


