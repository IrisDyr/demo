
print("Enter user stories to the notebook")
numbers1 = input().split(",")     #we can add multiple stories separated by comma
notebook = list(numbers1)        #filling the notebook a.k.a the list
print(notebook)

acti = input("1. Add user stories, 2. Delete user stories ")   #choosing what to do with the list 
if acti == '1':              #updating the notebook
    numbers = input().split(",")       #adding multiple stories
    notebook.extend(numbers)            #filling the list
    print(notebook)                    #printing the updated list
else:
    numbers2 = input()        #inputing a user story
    notebook.remove(numbers2)       #deleting a user story from the notebook
    print(notebook)               #printing the updated list

