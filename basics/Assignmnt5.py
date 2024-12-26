task=' '
todo_list=[]
while task != 'over':
    task=input('please pass the task todo else enter over : ')
    if task != 'over':
        todo_list.append(task)
print(todo_list)
