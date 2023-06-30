from django.http import HttpResponse
from django.shortcuts import render

import datetime
def home(request):
    date=datetime.datetime.now()
    isActive=True
    name="LearnCodeWithDurgesh"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'LUCKNOW'
    }
    #return HttpResponse("<h1>Hello Index Page</h1>"+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student,
    }
    return render(request,"home.html",{})

def about(request):
    #return HttpResponse("<h1>Hello About Page</h1>")
    return render(request,"about.html",{})
def services(request):
    #return HttpResponse("<h1>Hello About Page</h1>")
    return render(request,"services.html",{})


    