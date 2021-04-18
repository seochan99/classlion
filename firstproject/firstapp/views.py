from django.shortcuts import render

def welcome(request):
    return render(request,"welcome.html")

def hello(request):
    userName = request.GET['name'] # 대괄호다 ! 
    return render(request,'hello.html',{'userName': userName})