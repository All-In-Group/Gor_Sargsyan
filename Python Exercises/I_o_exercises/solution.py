#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        if my_func(*args,**kwargs) is None:
            print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
            print("{")
            my_func(*args,**kwargs)
            print("}\n")
        else:
            print("{")
            print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
            print(f"{my_func(*args,**kwargs)}")
            print("}\n")
    return wrapper
    
#Question 1
@show_solution
def in_out_func_1(x,y):
    return x * y

in_out_func_1(x = int(input()),y = int(input()))

#Question 2
@show_solution
def in_out_func_2(*args):
    print(*args,sep = "**")

in_out_func_2("Python","exercise")

#Question 3
@show_solution
def in_out_func_3(num):
    result = "".join([oct(num)[i] for i in range(len(oct(num))) if i > oct(num).index('o')])
    return int(result)

in_out_func_3(200)

#Question 4
@show_solution
def in_out_func_4(num,n):
    string = "".join([str(num)[i] for i in range(len(str(int(num)))+ 1 + n)])
    return float(string)
    #With this solution you can change lenght of numbers after point

in_out_func_4(20.2323,2)

#Question 5
@show_solution
def in_out_func_5(lenght:int):
    arr = []
    for _ in range(0,lenght):
        arr.append(float(input()))
    return arr

in_out_func_5(int(input()))

#Question 6
@show_solution
def in_out_func_6(file_path:str,new_file_path,index):
    count = 0
    with open(file_path, "r") as myfile:
        lines = myfile.readlines()
        count = len(lines)
        print(count)
    with open(new_file_path, "w") as myfile:
        for line in range(count):
            if line == index-1:
                continue
            else:
                myfile.write(lines[line])





#Question 7
string_1,string_2,string_3 = "Python programming language".split()
# list unpacking
print(string_1,string_3)

#Question 8
@show_solution
def in_out_func_8(total_money,price):
    print(f"I have {total_money} dollars so I can buy {total_money//price} football for {price:.2f} dollars.")

in_out_func_8(1900,40)

#Question 9
import os
def in_out_func_9(path:str):
    file_lenght = os.stat(path).st_size 
    return file_lenght == 0

#Question 10

def in_out_func_10(myfile,line:int):
    with open(myfile,"r") as file:
        lines = file.readlines()
    try:
        print(lines[line-1])
    except:
        print("please enter the valid number")





