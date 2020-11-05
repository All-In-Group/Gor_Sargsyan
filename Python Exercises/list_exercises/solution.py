#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print("{")
        print(f"{my_func(*args,**kwargs)}")
        print("}\n")
    return wrapper
#Question 1
@show_solution
def list_func_1(arr):
    return arr[::-1]

aLsit = [100, 200, 300, 400, 500]

list_func_1(aLsit)

#Question 2
@show_solution
def list_func_2(arr1,arr2):
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list_func_2(list1,list2)
    
#Question 3
@show_solution
def list_func_3(arr):
    return [i**2 for i in arr]

arr = [1, 2, 3, 4, 5, 6, 7]
list_func_3(arr)

#Question 4
@show_solution
def list_func_4(arr1,arr2):
    arr = []
    for i in list1:
        for j in list2:
            arr.append(i+j)
    return arr

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list_func_4(list1,list2)

#Question 5
@show_solution
def func_list_5(arr1,arr2):
    [print(i[0],i[1]) for i in  zip(arr1,arr2[::-1])]
    return ""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
    
func_list_5(list1,list2)

#Question 6
@show_solution
def list_func_6(arr):
    return [i for i in arr if len(i) > 0]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

list_func_6(list1)

#Question 7
@show_solution
def list_func_7(arr,num):
    for i in range(len(arr)):
        if type(arr[i]) == list:
            for j in range(len(arr[i])):
                if type(arr[i][j]) == list:
                    arr[i][j].append(num)
    return arr

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list_func_7(list1,7000)

#Question 8
@show_solution
def list_func_8(arr,subarr:list):
    for i in range(len(arr)):
        if type(arr[i]) == list:
            for j in range(len(arr[i])):
                if type(arr[i][j]) == list:
                    for x in range(len(arr[i][j])):
                        if type(arr[i][j][x]) == list:
                            for item in subarr:
                                arr[i][j][x].append(item)
    return arr
                                
arr = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subarr = ["h","i","j"]      

list_func_8(arr,subarr)

#Question 9
@show_solution
def list_func_9(arr,value,change_value):
    arr[arr.index(value)] = change_value
    return arr
list1 = [5, 10, 15, 20, 25, 50, 20]

list_func_9(list1,20,200)

#Question 10
@show_solution
def list_func_10(arr,value):
    return [i for i in arr if i != value]

list_func_10(list1,200)
