
def adding(x,y):   #sum
    return x + y

def substracting(x,y):  #substraction
    return x - y

def divide(x,y):    #division
    return x / y

def multiplication(x, y):   #multiplication
    return x * y

num1 = int(input("Input the first number  "))     #inputing values
num2 = int(input("Input the second number  "))
acti = int(input("What would you like to do? 1.Add 2.Substract 3.Divide 4. Multiplication "))  # choosing what to do with the numbers inputed

if acti == 1:                                         #telling the calculator which function to execute
   print(num1,"+",num2,"=", adding(num1,num2))

elif acti == 2:
   print(num1,"-",num2,"=", substracting(num1,num2))

elif acti == 3:
   print(num1,"/",num2,"=", divide(num1,num2))

else:
   print(num1,"*",num2,"=", multiplication(num1,num2))
