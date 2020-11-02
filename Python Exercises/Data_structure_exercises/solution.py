#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print("{")
        my_func(*args,**kwargs)
        print("}\n")
    return wrapper
#Question 1

@show_solution
def data_func_1(list_odd,list_even):
    print(f"Element at odd-index positions from list one {list_odd[1::2]}")
    print(f"Element at even-index positions from list two {list_even[0::2]}")
    list_mix = [*list_odd[1::2],*list_even[0::2]]
    print(f"Printing Final third list {list_mix}")

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

data_func_1(listOne,listTwo)

#Question 2
@show_solution
def data_func_2(arr,index,add_index = 2):
    print(f"Original list {arr}")
    tmp = arr.pop(index)
    print(f"List After removing element at index {index}  {arr}")
    arr.insert(add_index,tmp)
    print(f"List after Adding element at index {add_index} {arr}")
    arr.append(tmp)
    print(f"List after Adding element at last {arr}")
    

data_func_2([34, 54, 67, 89, 11, 43, 94],4,2)

#Question 3

@show_solution
def data_func_3(arr):
    print(f"Original list {arr}") 
    arr1 , arr2 , arr3 = [],[],[]
    split_num = len(arr)//3
    for _ in range(split_num):
        arr1.append(arr.pop(0))
    for _ in range(split_num):
        arr2.append(arr.pop(0))
    for _ in range(split_num):
        arr3.append(arr.pop(0))
    print(f"Chunk  1 {arr1}\nAfter reversing it {arr1[::-1]}")
    print(f"Chunk  2 {arr2}\nAfter reversing it {arr2[::-1]}\nChunk  3 {arr3}\nAfter reversing it {arr3[::-1]}")

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
data_func_3(sampleList)
        
#Question 4
@show_solution
def data_func_4(arr):
    print(f"Original list {arr}")
    print(f"Printing count of each item { {i:arr.count(i) for i in arr} }")

arr = [11, 45, 8, 11, 23, 45, 23, 45, 89]
data_func_4(arr)

#Question 5

@show_solution
def data_func_5(arr1,arr2):
    print("First List ", arr1)
    print("Second List ", arr2)
    result = set()
    for i in arr2:
        for j in arr1:
            if j**2 == i:
                result.add((j,i))
    # resultSet = set(result)
    print(f"Result is {result}")

arr1 = [2, 3, 4, 5, 6, 7, 8]
arr2 = [4, 9, 16, 25, 36, 49, 64]

data_func_5(arr1,arr2)

#Question 6

@show_solution
def data_func_6(set1,set2):
    print(f"First set {set1}\nSecond set {set2}")
    print(f"intersection is {set1.intersection(set2)}")
    print(f"First Set after removing common element {set1.difference(set2)}")

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 =  {67, 73, 43, 48, 83, 57, 29}
data_func_6(set1,set2)

#Question 7

@show_solution
def data_func_7(set1,set2):
    print(f"First Set  {set1}")
    print(f"Second Set {set2}")
    print(f"First set is subset of second set - {set1.issubset(set2)}")
    print(f"Second set is subset of first set - {set2.issubset(set1)}")
    print(f"First set is Super set of second set - {set1.issuperset(set2)}")
    print(f"Second set is Super set of first set - {set2.issuperset(set1)}")
    if set1.issubset(set2):
        set1 = set()
    else:
        set2 = set()
    print(f"First Set {set1}")
    print(f"Second Set {set2}")

firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
data_func_7(secondSet,firstSet)

#Question 8

@show_solution
def data_func_8(arr_num,arr_dict):
    print(f"After removing unwanted elemnts from list {[i for i in arr_num if i in arr_dict.values()]}")

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97,100]
sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
data_func_8(rollNumber,sampleDict)

#Question 9

@show_solution
def data_func_9(arr_dict):
    arr = []
    for i in arr_dict.values():
        if not(i in arr):
            arr.append(i)
    print(arr)

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
data_func_9(speed)

#Question 10

@show_solution
def data_func_10(arr):
    unique_arr = list()
    for i in arr:
        if not(i in unique_arr):
            unique_arr.append(i)
    print(f"Unique items {unique_arr}")
    print(f"Tuple {tuple(unique_arr)}")
    print(f"min : {min(unique_arr)}")
    print(f"max : {max(unique_arr)}")    

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
data_func_10(sampleList)