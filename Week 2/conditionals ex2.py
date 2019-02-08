outlist = ["John", "Jack", "Jim", "Johnny"]



def my_func(username):
    if username in outlist:
        print("It is in the list")
    else:
        print("It is not in the list")

my_func("John")