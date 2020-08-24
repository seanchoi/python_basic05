from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'employees/employee.html')    

def postGet(request):
    if request.method=="POST":
        valueOne = request.POST['one']
        valueTwo = request.POST['two']

    context = {
        "one" : valueOne,
        "two" : valueTwo
    }

    return render(request, 'employees/value.html', context)