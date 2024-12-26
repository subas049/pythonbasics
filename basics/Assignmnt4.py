num_list=[-1,4,-5,6,8,-3,1,6,-7,6,7,0]
positive_num=[]
negative_num=[]
for num in num_list:
    if num >=0:
        positive_num.append(num)
    else:
        negative_num.append(num)
result=positive_num+negative_num
print(result)

