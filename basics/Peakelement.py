num_list=[8,2,3,1,0,5,4,7,6,9]
n=len(num_list)
print(n)
for i in range(n):
    if i == 0 and num_list[i] > num_list[i + 1]:
        print(num_list[i])
    elif i == n-1 and num_list[i] > num_list[i -1]:
        print(num_list[i])
    elif num_list[i] > num_list[i + 1] and num_list[i] > num_list[i - 1]:
        print(num_list[i])

print('completed')

for i in range(5):
    print(i)



