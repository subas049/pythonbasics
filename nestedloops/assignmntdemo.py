str_ip='34,5,3,4,6'

num_lis=[]

for i in str_ip:
    if i == ',':
        continue
    num_lis.append(i)
print(num_lis)
