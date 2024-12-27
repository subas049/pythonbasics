
def removeduplicates(string_dulicate):
    newstr=''
    for char in string_dulicate:
        if char not in newstr:
            newstr=newstr+char
    return newstr

def dupcount(string_dulicate):
    newstr=''
    for i in string_dulicate:
        count=0
        if i not in newstr:
            newstr=newstr+i
            for j in range(len(string_dulicate)):
                if i==string_dulicate[j]:
                    count+=1
            print(i+' : '+str(count))
    print(newstr)


print(removeduplicates('SubashSubashP'))
print(dupcount('SubashSubashP'))
