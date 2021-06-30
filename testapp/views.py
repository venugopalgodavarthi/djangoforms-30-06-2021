from django.shortcuts import render
from testapp.forms import loginform 
# Create your views here.
def login(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"login.html")


def loginsample(request):
    form = loginform()
   # print(form)# it print the html tags
    if request.method=="POST":
        print(request.POST)     #it print userinput only (querydict)
        print(loginform(request.POST))  #it will display the htmltags with userinput values
        form = loginform(request.POST)
        print("diplay the user values")
        print("USERNAME=",request.POST.get('username')) #your getting the values
        print("password=",request.POST.get('password'))
        print("phone=",request.POST.get('phone'))
        print("address=",request.POST.get('address'))
        print("img=",request.POST.get('img'))
    return render(request,"loginform.html",{"appform":form})

