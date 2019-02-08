student = {"name":"Iris","school":"Dyrmishi", "grades":[100, 85, 60] }

def my_function(student):
    for mystudent in student:
        average = sum(student["grades"]) / len(student["grades"])
        return average

print(my_function(student))
