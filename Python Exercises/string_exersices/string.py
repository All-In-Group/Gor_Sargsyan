#Question 1
def middle_string(string):
    mid = len(string)//2
    return string[mid-1:mid+2]
print(middle_string("JaSonAy"))

#Question 2

def string_merge_mid(s1,s2):
    return f"{s1[:len(s1)//2]}{s2}{s1[len(s1)//2::]}"

print(string_merge_mid("parsik","avo"))

#Question 3
def string_merge(s1,s2):
    return f"{s1[0]}{s2[0]}{s1[len(s1)//2]}{s2[len(s2)//2]}{s1[-1]}{s2[-1]}"

print(string_merge("America","Japan"))

#Question 4
def lowers_first(string):
    return f'{"".join([i for i in string if i.lower() == i])}{"".join([i for i in string if i.upper() == i])}'
print(lowers_first("PyNaTive"))

#Question 5
def count_char_num_symb(string):
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
    print(f"Chars :{char}\nDigits :{num}\nSymbols :{symb}")

count_char_num_symb("P@#yn26at^&i5ve")
#Question 6

def reversed_mix(s1,s2):
    short = s1 if len(s1) < len(s2) else s2[::-1]
    long = s1 if len(s1) > len(s2) else s2[::-1]
    result =  "".join([f"{s1[i]}{s2[::-1][i]}" for i in range(len(short))])
    return f"{result}{long[len(short)::]}"


print(reversed_mix("Johny","depp"))

#Question 7

def isBalanced(s1,s2):
    short = s1 if len(s1) < len(s2) else s2
    long = s1 if len(s1) > len(s2) else s2
    for i in range(len(short)):
        if not(short[i] in long):
            return False
    return True
s1 = "Ynf"
s2 = "PYnative"
print(isBalanced(s1,s2))

#Question 8

def word_counter(string,word):
    print(f"The {word} count is: {string.lower().count(word.lower())}")

word_counter("Welcome to USA. usa awesome, isn't it?","usa")

#Question 9
def num_finding(string):
    numeric_list = "".join([i if i.isnumeric() else " " for i in string]).split()
    int_list = [int(i) for i in numeric_list]
    print(f"sum is {sum(int_list)}\naverge is {sum(int_list)/len(int_list)}")
    
num_finding( "English = 78 Science = 83 Math = 68 History = 65")

#Question 10
def letter_count(string):
    return  {i:string.count(i) for i in string}

print(letter_count("Apple"))

#Question 11
def reverse(string):
    return string[::-1]

print(reverse("string"))

#Question 12
str1 = "Emma is a data scientist who knows Python. Emma works at google."
def laststring_index(string,word):
    while string.lower().count(word.lower()) > 1:
        string = string.lower().replace(word.lower()," "*len(word),1)
    return string.index(word.lower())
    
        
    
print(laststring_index(str1,"emma"))

#Question 13
str1 = "Emma-is-a-data-scientist"

def eachsub(string):
    [print(i) for i in string.split("-")]
eachsub(str1)

#Question 14
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
def remove_empty(arr):
    return [i for i in str_list if type(i) == str and len(i) > 0]

print(remove_empty(str_list))

#Question 15
str1 = "/*Jon is @developer &**&*&@#)!@# musician"

def remove_punctuations(string):
    result_string = "".join([i for i in string if i.lower() != i.upper() or i == " "]).split()
    return "".join([f"{i} " for i in result_string])

print(remove_punctuations(str1))
#regex solution 
import re
def remove_punct_re(string):
    result_1 = re.sub(r"\W+"," ",string)
    result_2 = re.sub(r"^\s","",result_1)
    return result_2
print(remove_punct_re(str1))

#Question 16
import re
str_2 = "I am 25 years and 10 months old"
def only_nums(string):
    result = re.sub(r"[^\d]","",string)
    return result

print(only_nums(str_2))

#Question 17
str1 = "Emma25 is Data scientist50 and AI Expert"

def word_with_nums(string):
    for word in string.split():
        tmp = False
        for j in word:
            if j in "0123456789":
                tmp = True
        if tmp:
            print(word)

word_with_nums(str1) 

#Question 18
str1 = '/*Jon is @developer & musician!!'
import re
def symbol_to_sharp(string):
    return re.sub(r"[^\s\w]","#",string)

print(symbol_to_sharp(str1))
