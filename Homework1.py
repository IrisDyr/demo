num1 = input("Input the first number  ")
num2 = input("Input the second number  ") 
action = input("What would you like to do? 1.Add 2.Substract 3.Divide 4. Multiplication")


def adding(x,y):
    return x + y
def substracting(x,y):
    return x - y
def divide(x,y):
    return x / y
def multiplication(x, y):
    return x * y


if action == 1:
    print(adding(num1,num2)
elif action == 2:
    print(bsubstracting(num1, num2))
elif action == 3:
    print(divide(num1,num2))
else:
    print(multiplication(num1,num2))