with open("C:\\Users\\DELL\\PycharmProjects\\LearnBasics\\Demo.txt") as file:
    txt=file.read()
    print(txt)
file.close()


with open("C:\\Users\\DELL\\PycharmProjects\\LearnBasics\\Demo.txt",'a') as file:
    file.write("Im updating the file.")
file.close()


