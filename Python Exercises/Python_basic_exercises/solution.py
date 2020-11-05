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
def basic_func_1(a:int,b:int):
    result = a * b
    if result > 1000:
        return f"The result is {a + b}"
    return f"The result is {result}"

basic_func_1(100,11)

#Question 2
#This function works with any list with numbers in it , not only with range
@show_solution
def basic_func_2(int_arr:list):
    arr = int_arr
    prev = 0
    for num in range(len(arr)):
        if num > 1:
            prev += 1
        print(f"Current number : {arr[num]} Previous number : {arr[prev]} Sum : {arr[num] + arr[prev]}")
        
basic_func_2([1,5,100,389,100,100])

#Question 3
@show_solution
def basic_func_3(string:str):
    [print(string[i]) for i in range(len(string)) if i % 2 == 0]

basic_func_3("pynative")

#Question 4
@show_solution
def basic_func_4(string:str,index:int):
    return string[index:]

basic_func_4("Gor",1)

#Question 5
@show_solution
def basic_func_5(arr:list):
    return arr[0] == arr[-1]
basic_func_5([10,10,20,10])

#Question 6
@show_solution
def basic_func_6(arr:list):
    [print(arr[i]) for i in range(len(arr)) if arr[i] % 5 == 0]

basic_func_6([10,20,11,100])

#Question 7
@show_solution
def basic_func_7(string:str,substr:str):
    print(f"{substr}: appeared {string.count(substr)} times")

basic_func_7("Emma is a good developer. Emma is a writer","Emma")

#Question 8
@show_solution
def basic_func_8(pattern:int):
    for i in range(1,pattern + 1):
        for _ in range(0,i):
            print(i,end=" ")
        print(end="\n")

basic_func_8(5)

#Question 9
@show_solution
def basic_func_9(num:int):
    if str(num) == str(num)[::-1]:
        print(f"original number {num}\n","The original and the reverse number is the same")
        return True
    print(f"original number {num}\n","The original and reverse number is not same")
    return False

basic_func_9(101)
#Question 10
@show_solution
def basic_func_10(arr1:list,arr2:list):
    mergedarr = []
    [mergedarr.append(i) for i in arr1 if i % 2 != 0]
    [mergedarr.append(i) for i in arr2 if i % 2 == 0]
    return mergedarr

basic_func_10([3,10,2,40,1],[2,4,7])

#Question 11
@show_solution
def basic_func_11(num:int):
    tmp = "".join([f"{i} " for i in str(num)[::-1]])
    return tmp

basic_func_11(1234)

#Question 12
@show_solution
def basic_func_12(money:int):
    income = 0
    if money <= 10000:
        income = 0
    elif money <= 20000:
        income += (money - 10000) * 10 / 100
    else:
        # second 10 000 
        income = 10000 * 10 / 100
        # last 
        income += (money-20000)  * 20 / 100
    return income

basic_func_12(49700)
#Question 13
@show_solution
def basic_func_13(num:int):
    for i in range(1,num+1):
        for x in range(1,num+1):
            if (i * x) < 10:
                print(f"{i * x}  " ,  end = " ")
            else:
                print(f"{i*x} " , end = " ")
        print(end = "\n")
basic_func_13(10)

#Question 14
@show_solution
def basic_func_14(pattern:str,num:int):
    lenght = num
    for _ in range(num+1):
        print(pattern * lenght)
        lenght -= 1

basic_func_14("*",10)

#Question 15
@show_solution
def basic_func_15(base,exp):
    tmp = 1
    for _ in range(exp):
        tmp *= base
    return tmp
basic_func_15(5,4)

