numlist=[1,2,3,4,5,6,7,8]


def sumofnumlist(numlist):
    if not numlist:
        return 0
    else:
        return numlist[0]+sumofnumlist(numlist[1:])

print(sumofnumlist(numlist))
