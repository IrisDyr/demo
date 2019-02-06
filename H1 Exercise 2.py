numbers = input().split(",")       #input from a series of number, separated by comma

calc = list(numbers)      #fillinf the list calc with the numbers from above
calc = list(map(int, calc))  #convert to a list of integers 

adding = sum(calc)   #sum of elements
counting = len(calc)    # number of elements
print("The sum of the elements is: " + str(adding))
print("Then number of numbers inputed is " + str(counting))