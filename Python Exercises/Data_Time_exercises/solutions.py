from datetime import datetime ,timedelta

from dateutil.relativedelta import *

import time
#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print("{")
        print(my_func(*args,**kwargs))
        print("}\n")
    return wrapper
#Question 1
@show_solution
def datetime_func_1():
    return datetime.now().date()

datetime_func_1()

#Question 2
@show_solution
def datetime_func_2(time_str):
    return datetime.strptime(time_str,"%b %d %Y %I:%M%p")

date_string = "Feb 25 2020 4:20PM"
datetime_func_2(date_string)

#Question 3
@show_solution
def datetime_func_3(date,minus_days):
    return date - timedelta(days = minus_days)

given_date = datetime(2020, 2, 25)
datetime_func_3(given_date,7)

#Question 4
@show_solution
def datetime_func_4(date):
    return datetime.strftime(date,"%A %d %B %Y")

given_date = datetime(2020, 2, 25)
datetime_func_4(given_date)

#Question 5
@show_solution
def datetime_func_5(date):
    return datetime.strftime(date,"%A")

given_date = datetime(2020, 7, 26)
datetime_func_5(given_date)

#Question 6
@show_solution
def datetime_func_6(date,days_to_add,hours_to_add):
    return date + timedelta(days=days_to_add,hours=hours_to_add)

given_date = datetime(2020, 3, 22, 10, 0, 0)

datetime_func_6(given_date,7,12)

#Question 7
@show_solution

def datetime_func_7():
    return round(time.time()*1000)

datetime_func_7()

#Question 8
@show_solution
def datetime_func_8(date):
    result = str(date) + " this is a string"
    print(type(result))
    return result

given_date = datetime(2020, 2, 25)
datetime_func_8(given_date)

#Question 9
@show_solution
def datetime_func_9(date,months_to_calculate):
    return date + relativedelta(months=+months_to_calculate)


given_date = datetime(2020, 2, 25).date()
datetime_func_9(given_date,4)

@show_solution
#Question 10
def datetime_func_10(date1,date2):
    if date1 > date2:
        result = date1 - date2
    else:
        result = date2 - date1
    return f"{result.days} days"

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

datetime_func_10(date_1,date_2)


