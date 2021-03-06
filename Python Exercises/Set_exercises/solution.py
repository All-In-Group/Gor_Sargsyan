#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        if my_func(*args,**kwargs) is None:
            print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
            print("{")
            my_func(*args,**kwargs)
            print("}\n")
        else:
            print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
            print("{")
            print(f"{my_func(*args,**kwargs)}")
            print("}\n")
    return wrapper

#Question 1
@show_solution
def set_func_1(my_set,arr):
    return {*my_set,*arr}

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

set_func_1(sampleSet,sampleList)
#Question 2

@show_solution
def set_func_2(my_set1,my_set2):
    return set1.intersection(my_set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set_func_2(set1,set2)

#Question 3
@show_solution
def set_func_3(my_set1,my_set):
    return {*set1,*set2}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set_func_3(set1,set2)

#Question 4
@show_solution
def set_func_4(my_set1,my_set2):
    return set1.difference(set2)

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set_func_4(set1,set2)


#Question 5
@show_solution
def set_func_5(my_set1,*args):
    for i in args:
        my_set1.remove(i)
    return my_set1

set1 = {10, 20, 30, 40, 50}
set_func_5(set1,10,20,30)


#Question 6
@show_solution
def set_func_6(my_set1,my_set2):
    return my_set1.symmetric_difference(my_set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set_func_6(set1,set2)



#Question 7
@show_solution
def set_func_7(my_set1,my_set2):
    result = my_set1.intersection(my_set2)
    if len(result) == 0:
        return f"Two sets have no items in common"
    else:
        return f"Two sets have items in common : {my_set1.intersection(my_set2)}"

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set_func_7(set1,set2)


#Question 8
@show_solution
def set_func_8(my_set1,my_set2):
    my_set1.symmetric_difference_update(my_set2)
    return my_set1

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set_func_8(set1,set2)


#Question 9
@show_solution
def set_func_9(my_set1,my_set2):
    my_set1.intersection_update(my_set2)
    return my_set1

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set_func_9(set1,set2)
