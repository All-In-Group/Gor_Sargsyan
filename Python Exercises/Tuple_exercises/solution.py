#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print(f"\t\t{my_func(*args,**kwargs)}\n")
    return wrapper

#Question 
@show_solution
def tuple_func_1(my_tuple):
    return my_tuple[::-1]

aTuple = (10, 20, 30, 40, 50)
tuple_func_1(aTuple)

#Question 2
@show_solution
def tuple_func_2(my_tuple,value):
    for item in my_tuple:
        if type(item) == list:
            if value in item:
                return value

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
tuple_func_2(aTuple,20)

#Question 3
@show_solution
def tuple_func_3(item):
    return (item,)

tuple_func_3("Asya")

#Question 4
#without a function
        
aTuple = (10, 20, 30, 40)
a,b,c,d  =  aTuple
print(f"Question 4 solution:\n\t\t{a}\n\t\t{b}\n\t\t{c}\n\t\t{d}")

#Question 5
#Without a function
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2 = tuple2,tuple1
print(f"Question 5 solution:\n\t\tTuple 1 {tuple1}\n\t\tTuple 2 {tuple2}")

#Question 6
@show_solution
def tuple_func_6(my_tuple,*args):
    arr = list()
    for i in my_tuple:
        if i in args:
            arr.append(i)
    return tuple(arr)
tuple1 = (11, 22, 33, 44, 55, 66)
tuple_func_6(tuple1,44,55)
#Question 7
@show_solution
def tuple_func_7(my_tuple):
    for i in my_tuple:
        if type(i) == list:
            i[0] = 222
    return my_tuple
tuple1 = (11, [22, 33], 44, 55)
tuple_func_7(tuple1)

#Question 8
@show_solution
def tuple_func_8(my_tuple):
    my_tuple = list(my_tuple)
    for _ in range(len(my_tuple)-1):
        for j in range(len(my_tuple)-1):
            if my_tuple[j][1] > my_tuple[j+1][1]:
                 my_tuple[j],my_tuple[j+1] = my_tuple[j+1],my_tuple[j]
    return tuple(my_tuple)

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple_func_8(tuple1)

#Question 9
@show_solution
def tuple_func_9(my_tuple,item):
    return list(my_tuple).count(item)

tuple1 = (50, 10, 60, 70, 50)
tuple_func_9(tuple1,50)

#Question 10
@show_solution
def tuple_func_10(my_tuple):
    for i in range(len(my_tuple)-1):
        if not(my_tuple[i] == my_tuple[i+1]):
            return False
    return True

tuple1 = (45, 45, 45, 45)
tuple_func_10(tuple1)