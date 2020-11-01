#Question 1

def name_age(name:str,age:int):
    print(name,age)
name_age("Gor",22)

#Question 2

def func1(*args):
    for i in args:
        print(i)

func1("arg1","arg2","arg3")

#Question 3

def calculation(arg1:int,arg2:int):
    return (arg1+arg2,arg1-arg2)

result = calculation(20,30)
print(result)

#Question 4

def showEmployee(name,salary = 9000):
    print(f"Employee {name.capitalize()}'s salary is: {salary}'")

showEmployee("Gor")

#Question 5

def outer_func(a,b):
    def inner_func(a,b):
        return a + b
    return inner_func(a,b) + 5

print(outer_func(10,10))

#Question 6

def sum_of_num(num):
    if num > 0:
        return num + sum_of_num(num-1)
    elif num < 0:
        return num + sum_of_num(num+1)
    else:
        return 0
print(sum_of_num(-10))

#Question 7
def displayStudent(name:str,age:int):
    print(name,age)

displayStudent("Gor",22)   
showStudent = displayStudent
showStudent("Gor",22)

#Question 8
def list_of_even_numbers(a,b):
    return [i for i in range(a,b) if i % 2 == 0]

print(list_of_even_numbers(4,30))
        
#Question 9
def largest_item(arr):
    return max(arr)

print(largest_item([1,2,3,4,5,6,100,2,3,45]))



