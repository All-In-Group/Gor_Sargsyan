#Python Basic Exercise for Beginners
#Question 1 

def multyply_sum(a:int,b:int):
    result = a * b
    if result > 1000:
        return f"The result is {a + b}"
    return f"The result is {result}"

print(multyply_sum(100,11))

#Question 2
#This function works with any list with numbers in it , not only with range

def sum_of_prev(int_arr:list):
    arr = int_arr
    prev = 0
    for num in range(len(arr)):
        if num > 1:
            prev += 1
        print(f"Current number : {arr[num]} Previous number : {arr[prev]} Sum : {arr[num] + arr[prev]}")
        
sum_of_prev([1,5,100,389,100,100])

#Question 3

def show_only_even(string:str):
    [print(string[i]) for i in range(len(string)) if i % 2 == 0]

show_only_even("pynative")

#Question 4
def string_change(string:str,index:int):
    return string[index:]

print(string_change("Gor",1))

#Question 5
def start_end_same(arr:list):
    return arr[0] == arr[-1]
print(start_end_same([10,10,20,10]))

#Question 6
def division_by_5(arr:list):
    [print(arr[i]) for i in range(len(arr)) if arr[i] % 5 == 0]

division_by_5([10,20,11,100])

#Question 7
def count_in_string(string:str,substr:str):
    print(f"{substr}: appeared {string.count(substr)} times")

count_in_string("Emma is a good developer. Emma is a writer","Emma")

#Question 8
def pattern_print(pattern:int):
    for i in range(1,pattern + 1):
        for _ in range(0,i):
            print(i,end=" ")
        print(end="\n")

pattern_print(5)

#Question 9
def pollindrom_check_num(num:int):
    if str(num) == str(num)[::-1]:
        print(f"original number {num}\n","The original and the reverse number is the same")
        return True
    print(f"original number {num}\n","The original and reverse number is not same")
    return False

pollindrom_check_num(101)
#Question 10

def odd_even_listmerge(arr1:list,arr2:list):
    mergedarr = []
    [mergedarr.append(i) for i in arr1 if i % 2 != 0]
    [mergedarr.append(i) for i in arr2 if i % 2 == 0]
    return mergedarr

print("List is ",odd_even_listmerge([3,10,2,40,1],[2,4,7]))    

#Question 11
def int_to_str(num:int):
    tmp = "".join([f"{i} " for i in str(num)[::-1]])
    return tmp

print("The result is " , int_to_str(1234))

#Question 12
def tax_count(money:int):
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

print("Tax is ",tax_count(49700))
#Question 13

def table(num:int):
    for i in range(1,num+1):
        for x in range(1,num+1):
            if (i * x) < 10:
                print(f"{i * x}  " ,  end = " ")
            else:
                print(f"{i*x} " , end = " ")
        print(end = "\n")
table(10)

#Question 14
def pattern_pyramid(pattern:str,num:int):
    lenght = num
    for _ in range(num+1):
        print(pattern * lenght)
        lenght -= 1

pattern_pyramid("*",10)

#Question 15
def exponent(base,exp):
    tmp = 1
    for _ in range(exp):
        tmp *= base
    return tmp
print(exponent(5,4))

