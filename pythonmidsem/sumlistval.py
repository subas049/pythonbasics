numlist=list(range(5))


def sumofnumlist(numlist):
    if not numlist:
        return 0
    else:
        return numlist[0]+sumofnumlist(numlist[1:])

print(sumofnumlist(numlist))
