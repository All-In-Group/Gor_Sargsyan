from django.shortcuts import render
import json
import requests
from json.decoder import JSONDecodeError

# Create your views here.
def create(request):
    if request.method == 'POST':
        pydict = dict(request.POST)
        print(request.POST)
        my_dict = {i : pydict[i] for i in pydict.keys() if not('csrf' in i)}
        with open('resume_app_resume/vitas.json') as jf:
            json_dict = json.load(jf)
            num = 1
            for i in json_dict.keys():
                if 'cv' in i:
                    num += 1
            json_dict[f'cv{num}'] = my_dict
        write_json(json_dict)
            
            
                    
            
    context = {}
    return render(request,'resumies/create_cv.html',context)

def write_json(data, filename='resume_app_resume/vitas.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


def home(request):
    with open('resume_app_resume/vitas.json','r') as jf:
        json_dict = json.load(jf)
    my_dict = {}
    for item in json_dict.keys():
        my_dict[item] = {i:json_dict[item][i] for i in 
            json_dict[item].keys() if i == "fullname" or i == "professionsInput"}
    context = {"vitas": my_dict}
    return render(request,'resumies/home.html',context)

def show_cv(request,pk):
    with open('resume_app_resume/vitas.json','r') as jf:
        json_dict = json.load(jf)
    cv_for_show = json_dict[pk]
    skill_set = {cv_for_show['skillname'][y]:cv_for_show['skilltext'][y] 
                                for y in  range(len(cv_for_show['skillname']))}
    work_set = dictmaker(cv_for_show,'companyname','position','data-field','aboutwork')
    education_set = dictmaker(cv_for_show,'education','education-data','educationfield','gpa')
    context = {
                "cv_for_show":cv_for_show,
                'skillset':skill_set,
                'expirience':work_set,
                'educations':education_set,
                }
    return render(request,'resumies/index.html',context)
    

def dictmaker(data,*args):
    work_data = {}
    namecount = 1
    keyname = 'exp1'
    for key in range(len(data[args[0]])):
        for i in work_data.keys():
            if i == keyname:
                namecount += 1
        keyname = f"{keyname[0:-1]}{namecount}"
        for arg in range(0,len(args)):
            if arg == 0:
                work_data[keyname] = {arg:data[args[arg]][key]}
            else:
                work_data[keyname].update({arg : data[args[arg]][key]})
    return work_data        
    

