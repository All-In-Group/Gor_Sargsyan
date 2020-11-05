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
def loop_func_1(Range:int):
    for i in range(Range+1):
        print(i)

loop_func_1(10)
#Question 2
@show_solution
def loop_func_2(start,end):
    for i in range(start,end):
        for x in range(1,i+1):
            print(x,end = " ")
        print(end = "\n")
loop_func_2(1,6)

#Question 3
@show_solution
def loop_func_3(num):
    summ = 0
    for i in range(num+1):
        summ += i
    print(summ)
    return summ

loop_func_3(12)

#Question 4
@show_solution
def loop_func_4(num,Range):
    num = 3
    multiply = 1
    for i in range(1,Range):
        multiply = i*num
        print(multiply)

loop_func_4(3,14)

    #Alternatively
@show_solution
def loop_func_alt_4(num,Range):
    for i in range(0,(Range*num),num):
        if i > 0: print(i)

loop_func_alt_4(3,14)


#Question 5
@show_solution
def loop_func_5(arr,num):
    for i in arr:
        if i > 150:
            break
        if i % num == 0:
            print(i)

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
loop_func_5(list1,5)

#Question 6
@show_solution
def loop_func_6(num):
    print(len(str(num)))

loop_func_6(49984)


#Question 7
@show_solution
def loop_func_7(num):
    for i in range(1,num+1)[::-1]:
        for j in range(1,i+1)[::-1]:
            print(j,end = " ")
        print()

loop_func_7(5)

#Question 8
@show_solution
def loop_func_8(arr):
    for i in arr[::-1]:
        print(i)

list1 = [10, 20, 30, 40, 50]
loop_func_8(list1)


#Question 9
@show_solution
def loop_func_9(start,stop):
    for i in range(start,stop,-1):
        print(-i)

loop_func_9(10,0)

#question 10
@show_solution
def loop_func_10(Range):
    for i in range(Range):
        print(i)
    print("done!")

loop_func_10(10)

#question 11
@show_solution
def loop_func_11(start,end):
    for i in range(start,end+1):
        half = i//2
        prime = True
        for j in range(2,half+1):
            if i % j == 0:
                prime = False
        if prime == True:
            print(i)

loop_func_11(25,50)

#Question 12
@show_solution
def loop_func_12(num):
    a,b= 0,1
    for _ in range(num):
        print(a)
        a,b = b,a+b

loop_func_12(10)
        
#Question 13
@show_solution
def loop_func_13(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    print(result)

loop_func_13(5)

#Question 14
@show_solution
def loop_func_14(num):
    reverse = 0
    while num != 0:
        lastchar = num % 10
        num = num // 10
        reverse = reverse * 10 + lastchar
    print(reverse)

loop_func_14(1998)
# Alternatively , faster and easier algorythm
@show_solution
def loop_func_alt_14(num):
    return int(str(num)[::-1])


loop_func_alt_14(1023)

#Question 15
@show_solution
def loop_func_15(arr):
    for i in range(0,len(arr),2):
        print(my_list[i],end = " ")
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
loop_func_15(my_list)

#Question 16
@show_solution
def loop_func_16(num):
    for i in range(num+1):
        print(f"Current Number is : {i}  and the cube is {i**3}")

loop_func_16(10)


#Question 17
@show_solution
def loop_func_17(number_of_terms):
    term_list = []
    for i in range(1,number_of_terms+1):
        term_list.append(int("2"*i))
    print(sum(term_list))
        
loop_func_17(5)

#Question 18
@show_solution
def loop_func_18(num):
    j = 0
    for i in range(num):
        if i <= num // 2:
            j+=1 
        else:
            j-=1
        print("*" * j)

loop_func_18(9)
