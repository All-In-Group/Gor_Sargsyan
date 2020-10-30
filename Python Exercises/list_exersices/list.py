#Question 1

def reverse_string(arr):
    return arr[::-1]

aLsit = [100, 200, 300, 400, 500]

print(reverse_string(aLsit))

#Question 2

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]

def concatanate(arr1,arr2):
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

print(concatanate(list1,list2))
    
#Question 3

def square(arr):
    return [i**2 for i in arr]

arr = [1, 2, 3, 4, 5, 6, 7]

print(square(arr))

#Question 4
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

def concatanate_words(arr1,arr2):
    arr = []
    for i in list1:
        for j in list2:
            arr.append(i+j)
    return arr
print(concatanate_words(list1,list2))

#Question 5

def func_list_1(arr1,arr2):
    [print(i[0],i[1]) for i in  zip(arr1,arr2[::-1])]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
    
func_list_1(list1,list2)

#Question 6
def remove_empty(arr):
    return [i for i in arr if len(i) > 0]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print(remove_empty(list1))

#Question 7
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
def add_in_list(arr,num):
    for i in range(len(arr)):
        if type(arr[i]) == list:
            for j in range(len(arr[i])):
                if type(arr[i][j]) == list:
                    arr[i][j].append(num)
    return arr

print(add_in_list(list1,7000))

#Question 8
def add_list_in_list(arr,subarr:list):
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

print(add_list_in_list(arr,subarr))

#Question 9
def find_change_value(arr,value,change_value):
    arr[arr.index(value)] = change_value
    return arr
list1 = [5, 10, 15, 20, 25, 50, 20]

print(find_change_value(list1,20,200))

#Question 10
def find_delete_value(arr,value):
    return [i for i in arr if i != value]

print(find_delete_value(list1,20))
