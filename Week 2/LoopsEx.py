

 def my_second():
     my_name = input("What is your name")

     cont = True
    while cont is True:
         for letter in my_name:
            print letter
    
        decision = input("Do you want to continue?")

        if decision =="n":  
            cont = False

my_second()