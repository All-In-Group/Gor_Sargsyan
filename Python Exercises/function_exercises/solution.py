#Question 1
#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print(f"\t\t{my_func(*args,**kwargs)}\n")
    return wrapper

@show_solution
def func_1(name:str,age:int):
    return f"{name,age}"
func_1("Gor",22)

#Question 2
@show_solution
def func_2(*args):
    print(*args,sep = "\n")
    return ""

func_2("arg1","arg2","arg3")


#Question 3
@show_solution
def func_3(arg1:int,arg2:int):
    return (arg1+arg2,arg1-arg2)

func_3(20,30)

#Question 4
@show_solution
def func_4(name,salary = 9000):
    return f"Employee {name.capitalize()}'s salary is: {salary}'"

func_4("Gor")

#Question 5
@show_solution
def func_5(a,b):
    def inner_func(a,b):
        return a + b
    return inner_func(a,b) + 5

func_5(10,10)

#Question 6
def func_6(num):
    if num > 0:
        return num + func_6(num-1)
    elif num < 0:
        return num + func_6(num+1)
    else:
        return 0
print(f"Question 6 solution :\n\t\t{func_6(-10)}")

#Question 7
@show_solution
def func_7(name:str,age:int):
    return f"{name,age}"

student_function_7 = func_7
student_function_7("Gor",22)

#Question 8
@show_solution
def func_8(a,b):
    return [i for i in range(a,b) if i % 2 == 0]

func_8(4,30)
        
#Question 9
@show_solution
def func_9(arr):
    return max(arr)

func_9([1,2,3,4,5,6,100,2,3,45])



