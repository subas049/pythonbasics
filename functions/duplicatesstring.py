def removeduplicates(string_dulicate):
    newstr = ''
    for char in string_dulicate:
        if char.lower() not in newstr.lower():
            newstr = newstr + char
    return newstr


def dupcount(string_dulicate):
    newstr = ''
    for i in string_dulicate:
        count = 0
        if i.lower() not in newstr.lower():
            newstr = newstr + i
            for j in range(len(string_dulicate)):
                if i.lower() == string_dulicate[j].lower():
                    count += 1
            if count > 1:
                print(i + ' : ' + str(count))
    print(newstr)


print(removeduplicates('SubashPSubashP'))
print(dupcount('SubashPSubashP'))
