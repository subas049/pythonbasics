def revstring(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + revstring(s[:-1])


print(revstring(input("Please enter a string to reverse it : ")))
