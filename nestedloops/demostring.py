str1='S,U,B,A,S,H, ,P'
str2=''

length=len(str1)
for i in str1:
    if i==',':
        continue
    str2=str2+i
print(str2)
