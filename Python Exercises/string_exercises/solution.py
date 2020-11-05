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
def str_func_1(string):
    mid = len(string)//2
    return string[mid-1:mid+2]

str_func_1("JaSonAy")

#Question 2
@show_solution
def str_func_2(s1,s2):
    return f"{s1[:len(s1)//2]}{s2}{s1[len(s1)//2::]}"

str_func_2("parsik","avo")

#Question 3
@show_solution
def str_func_3(s1,s2):
    return f"{s1[0]}{s2[0]}{s1[len(s1)//2]}{s2[len(s2)//2]}{s1[-1]}{s2[-1]}"

str_func_3("America","Japan")

#Question 4
@show_solution
def str_func_4(string):
    return f'{"".join([i for i in string if i.lower() == i])}{"".join([i for i in string if i.upper() == i])}'

str_func_4("PyNaTive")

#Question 5
@show_solution
def str_func_5(string):
    char = 0
    num = 0
    symb = 0
    for i in  string:
        if i.lower() != i.upper():
            char += 1
        elif i.isnumeric():
            num += 1
        else:
            symb += 1
    return(f"Chars :{char}\nDigits :{num}\nSymbols :{symb}")

str_func_5("P@#yn26at^&i5ve")
#Question 6
@show_solution
def str_func_6(s1,s2):
    short = s1 if len(s1) < len(s2) else s2[::-1]
    long = s1 if len(s1) > len(s2) else s2[::-1]
    result =  "".join([f"{s1[i]}{s2[::-1][i]}" for i in range(len(short))])
    return f"{result}{long[len(short)::]}"


str_func_6("Johny","depp")

#Question 7
@show_solution
def str_func_7(s1,s2):
    short = s1 if len(s1) < len(s2) else s2
    long = s1 if len(s1) > len(s2) else s2
    for i in range(len(short)):
        if not(short[i] in long):
            return False
    return True
s1 = "Ynf"
s2 = "PYnative"
str_func_7(s1,s2)

#Question 8
@show_solution
def str_func_8(string,word):
    result = string.lower().count(word.lower())
    return f"The {word} count is: {result}"

str_func_8("Welcome to USA. USA awesome, isn't it?","USA")

#Question 9
@show_solution
def str_func_9(string):
    numeric_list = "".join([i if i.isnumeric() else " " for i in string]).split()
    int_list = [int(i) for i in numeric_list]
    return f"sum is {sum(int_list)}\naverge is {sum(int_list)/len(int_list)}"
    
str_func_9( "English = 78 Science = 83 Math = 68 History = 65")

#Question 10
@show_solution
def str_func_10(string):
    return  {i:string.count(i) for i in string}

str_func_10("Apple")

#Question 11
@show_solution
def str_func_11(string):
    return string[::-1]

str_func_11("string")

#Question 12
@show_solution

def str_func_12(string,word):
    while string.lower().count(word.lower()) > 1:
        string = string.lower().replace(word.lower()," "*len(word),1)
    return string.index(word.lower())
    
str1 = "Emma is a data scientist who knows Python. Emma works at google."   
str_func_12(str1,"emma")

#Question 13
@show_solution
def str_func_13(string):
    [print(i) for i in string.split("-")]
    return ""

str1 = "Emma-is-a-data-scientist"
str_func_13(str1)
#Question 14
@show_solution
def str_func_14(arr):
    return [i for i in str_list if type(i) == str and len(i) > 0]
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str_func_14(str_list)

#Question 15

@show_solution
def str_func_15(string):
    result_string = "".join([i for i in string if i.lower() != i.upper() or i == " "]).split()
    return "".join([f"{i} " for i in result_string])

str1 = "/*Jon is @developer &**&*&@#)!@# musician"
str_func_15(str1)
#regex solution 
import re
@show_solution
def str_func_re_15(string):
    result_1 = re.sub(r"\W+"," ",string)
    result_2 = re.sub(r"^\s","",result_1)
    return result_2
str_func_re_15(str1)

#Question 16
@show_solution

def str_func_16(string):
    result = re.sub(r"[^\d]","",string)
    return result

str_2 = "I am 25 years and 10 months old"
str_func_16(str_2)

#Question 17
@show_solution
def str_func_17(string):
    words = []
    for word in string.split():
        tmp = False
        for j in word:
            if j in "0123456789":
                tmp = True
        if tmp:
            words.append(word)
    return words

str1 = "Emma25 is Data scientist50 and AI Expert"
str_func_17(str1) 

#Question 18
@show_solution
def str_func_18(string):
    return re.sub(r"[^\s\w]","#",string)

str1 = '/*Jon is @developer & musician!!'
str_func_18(str1)