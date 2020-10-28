#Question 1
def input_multiply(x,y):
    return x * y

print(input_multiply(x = int(input()),y = int(input())))

#Question 2

def seperator_of_string(*args):
    print(*args,sep = "**")

seperator_of_string("Python","exercise")

#Question 3

def dec_to_oct(num):
    result = "".join([oct(num)[i] for i in range(len(oct(num))) if i > oct(num).index('o')])
    return int(result)


#Question 4
def float_round(num,n):
    string = "".join([str(num)[i] for i in range(len(str(int(num)))+ 1 + n)])
    return float(string)
    #With this solution you can change lenght of numbers after point

print(float_round(20.2323,2))

#Question 5

def float_list_input(lenght):
    arr = []
    for _ in range(0,lenght):
        arr.append(float(input()))
    return arr

print(float_list_input(int(input())))

#Question 6
def without_some_line(file_path:str,new_file_path,index):
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
def show_data(total_money,price):
    print(f"I have {total_money} dollars so I can buy {total_money//price} football for {price:.2f} dollars.")

show_data(1900,40)

#Question 9
import os
file_lenght = os.stat("your\\file\\pathgi").st_size 
print(file_lenght == 0)

#Question 10

def line_reader(myfile,line:int):
    with open(myfile,"r") as file:
        lines = file.readlines()
    try:
        print(lines[line-1])
    except:
        print("please enter the valid number")

line_reader("your\\path",10)