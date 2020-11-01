#Question 1
for i in range(11):
    print(i)

#Question 2

for i in range(1,6):
    for x in range(1,i+1):
        print(x,end = " ")
    print(end = "\n")

#Question 3
def sum_of_all(num):
    summ = 0
    for i in range(num+1):
        summ += i
    print(summ)
    return summ
sum_of_all(10)

#Question 4
n = 2
multiply = 1
for i in range(1,11):
    multiply = i*n
    print(multiply)

    #Alternatively
for i in range(0,(11*n),n):
    if i > 0: print(i)

#Question 5
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
def find_dev_by_num(arr,num):
    for i in arr:
        if i > 150:
            break
        if i % num == 0:
            print(i)
        
find_dev_by_num(list1,5)

#Question 6

num = 456667
print(len(str(num)))

#Question 7
def num_pyramide_rev(num):
    for i in range(1,num+1)[::-1]:
        for j in range(1,i+1)[::-1]:
            print(j,end = " ")
        print()

num_pyramide_rev(5)

#Question 8
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)

#Question 9
for i in range(10,0,-1):
    print(-i)

#question 10

for i in range(5):
    print(i)
print("done!")

#question 11
def primenums(start,end):
    for i in range(start,end+1):
        half = i//2
        prime = True
        for j in range(2,half+1):
            if i % j == 0:
                prime = False
        if prime == True:
            print(i)

primenums(25,50)

#Question 12

def fibonacci(num):
    a,b= 0,1
    for _ in range(num):
        print(a)
        a,b = b,a+b
fibonacci(10)
        
#Question 13
def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    print(result)

factorial(5)

#Question 14

def reverse_num(num):
    reverse = 0
    while num != 0:
        lastchar = num % 10
        num = num // 10
        reverse = reverse * 10 + lastchar
    print(reverse)
    return reverse
# Alternatively , faster and easier algorythm
def reverse_num_easy(num):
    return int(str(num)[::-1])

reverse_num(1023)
print(reverse_num_easy(1023))

#Question 15
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(0,len(my_list),2):
    print(my_list[i],end = " ")

#Question 16
input_number = 6
for i in range(input_number+1):
    print(f"Current Number is : {i}  and the cube is {i**3}")
    
#Question 17
def sum_of_terms(number_of_terms):
    term_list = []
    for i in range(1,number_of_terms+1):
        term_list.append(int("2"*i))
    print(sum(term_list))
        
sum_of_terms(5)

#Question 18

def drawing_pattern(num):
    j = 0
    for i in range(num):
        if i <= num // 2:
            j+=1 
        else:
            j-=1
        print("*" * j)

drawing_pattern(9)
