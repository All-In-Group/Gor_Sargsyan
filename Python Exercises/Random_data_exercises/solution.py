import random
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print("{")
        print(my_func(*args,**kwargs))
        print("}\n")
    return wrapper

#Question1
@show_solution
def random_func_1(num1,num2,div=5):
    arr = []
    for _ in range(3):
        num = random.randrange(num1,num2)
        while num%div!=0:
            num = random.randrange(num1,num2)
        arr.append(num)
    return arr

random_func_1(100,900)

#Question2
@show_solution
def random_func_2(num1):
    arr = []
    for _ in range(num1):
        num = random.randrange(1000000000,10000000000)
        while num in arr:
            num = random.randrange(1000000000,10000000000)
        arr.append(num)
    return random.sample(arr,2)

random_func_2(100)
    
#Question 3
import secrets
@show_solution
def random_func_3(dig):
    secret_rand = secrets.SystemRandom()
    otp = secret_rand.randrange(int(str("1"+"0"*(dig-1))),int(str("1"+"0"*(dig))))
    return f"Random OTP is {otp}"

random_func_3(6)

#Question 4
@show_solution
def random_func_4(string):
    return random.choice(string)

random_func_4("Gor")

#Question 5
import string
@show_solution
def random_func_5(dig):
    letters = string.ascii_lowercase+string.ascii_uppercase
    return "".join([random.choice(letters) for _ in range(dig)])

random_func_5(5)

#Question 6
@show_solution
def random_func_6():
    password = []
    password += random.sample(string.ascii_letters + string.digits + string.punctuation,6)
    password += random.sample(string.ascii_uppercase,2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    random.shuffle(password)
    return "".join([i for i in password])

random_func_6()

#Question 7
@show_solution
def random_func_7():
    first_num = random.random()
    second_num = random.uniform(9.5,99.5)
    return first_num*second_num

random_func_7()
        
#Question 8
@show_solution
def random_func_8():
    result = secrets.token_urlsafe(64)
    print("64 byte url token is")
    return result

random_func_8()

#Question 9
@show_solution
def random_func_9():
    arr = list(range(10))
    for _ in range(5):
        random.seed(10000)
        print(random.choice(arr),end = " ")
    return ""

random_func_9()