
def adding(x,y):
    return x + y

def substracting(x,y):
    return x - y

def divide(x,y):
    return x / y

def multiplication(x, y):
    return x * y

num1 = int(input("Input the first number  "))
num2 = int(input("Input the second number  "))
acti = int(input("What would you like to do? 1.Add 2.Substract 3.Divide 4. Multiplication "))

if acti == 1:
   print(num1,"+",num2,"=", adding(num1,num2))

elif acti == 2:
   print(num1,"-",num2,"=", substracting(num1,num2))

elif acti == 3:
   print(num1,"/",num2,"=", divide(num1,num2))

else:
   print(num1,"*",num2,"=", multiplication(num1,num2))
