#Wrapper function for better answer visibility 
def show_solution(my_func):
    def wrapper(*args,**kwargs):
        print(f"Question {[i for i in my_func.__name__.split('_') if i.isdigit()][0]} : solution")
        print(f"\t\t{my_func(*args,**kwargs)}\n")
    return wrapper

#Question 1

@show_solution
def dict_func_1(arr_1,arr_2):
    return {arr_1[i]:arr_2[i] for i in range(len(keys))}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_func_1(keys,values)

#Question 2

@show_solution
def dict_func_2(dict_1,dict_2):
    dict3 = {**dict1,**dict2}
    return dict3
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict_func_2(dict1,dict2)
    
#Question 3
@show_solution


def dict_func_3(dict1,name):
    for i in dict1.values():
        if type(i) == dict:
            for j in i.values():
                if type(j) == dict:
                    for x in j.values():
                        if  type(x) == dict:
                            return x[name]
                        
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
dict_func_3(sampleDict,"history")

#Question 4
@show_solution
def dict_func_4(arr:list , dict1:dict):
    return {i:dict1 for i in arr}

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

dict_func_4(employees,defaults)


#Question 5
@show_solution
def dict_func_5(arr:list,dict1:dict):
    return {i:dict1[i] for i in arr}

sampleDict = { "name": "Kelly", "age":25,"salary": 8000,"city": "New york" }
key_list = ["name","salary"]

dict_func_5(key_list,sampleDict)

#Question 6
@show_solution
def dict_func_6(arr:list,dict1:dict):
    return {i:dict1[i] for i in dict1.keys() if not(i in arr)}

sampleDict = { "name": "Kelly", "age":25,"salary": 8000,"city": "New york" }
key_list = ["name","salary"]

dict_func_6(key_list,sampleDict)

#Question 7
@show_solution
def dict_func_7(dict1:dict,value):
    return  value in dict1.values()

sampleDict = {'a': 100, 'b': 200, 'c': 300}
dict_func_7(sampleDict,200)
    

#Question 8
@show_solution
def dict_func_8(dict1:dict,key,rename_key):
    dict1[rename_key] = dict1.pop(key)
    return dict1
sampleDict = { "name": "Kelly", "age":25,"salary": 8000,"city": "New york" }

dict_func_8(sampleDict,"city","location")

#Question 9
@show_solution
def dict_func_9(dict1:dict):
    for key in dict1.keys():
        if dict1[key] == min(dict1.values()):
            return key

sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

dict_func_9(sampleDict)

#Question 10
@show_solution
def dict_func_10(dict1:dict,name:str,changed_salary:int):
    for key in dict1.keys():
        if name in dict1[key].values():
            if "salary" in dict1[key].keys():
                dict1[key]["salary"] = changed_salary
    return dict1
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
dict_func_10(sampleDict,"Brad",150000000)