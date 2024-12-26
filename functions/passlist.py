def printlist(name_list):
    for i in name_list:
        print(i.title())


printlist(['subash', 'vadivel', 'nagaraj', 'suresh', 'moorthy'])


def userDetails(details):
    name=details[0]
    age=details[1]
    gender=details[2]
    education=details[3]
    user={'name': name , 'age': age, 'gender': gender, 'education': education}
    return user

print(userDetails(['subash','38','male','mtech']))
