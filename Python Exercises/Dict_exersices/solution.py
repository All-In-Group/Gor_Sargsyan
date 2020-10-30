#Question 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def dict_func_1(arr_1,arr_2):
    return {arr_1[i]:arr_2[i] for i in range(len(keys))}

print(dict_func_1(keys,values))

#Question 2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def dict_func_2(dict_1,dict_2):
    dict3 = {**dict1,**dict2}
    return dict3

print(dict_func_2(dict1,dict2))    
    
#Question 3
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
print(sampleDict["class"])
def dict_func_3(dict1,name):
    for i in dict1.values():
        if type(i) == dict:
            for j in i.values():
                if type(j) == dict:
                    for x in j.values():
                        if  type(x) == dict:
                            print(x[name])
                        

dict_func_3(sampleDict,"history")
