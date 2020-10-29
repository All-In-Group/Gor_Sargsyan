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

#

    
    