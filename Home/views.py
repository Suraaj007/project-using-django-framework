from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable1':"suraj is great",
        'variable2':"harry is great"
    }
    #return HttpResponse('This is homepage')
    return render(request,'index.html',context)
def about(request):
    #return HttpResponse('This is about page') 
    return render(request,'about.html')   
def services(request):
    #return   HttpResponse('This is service page')
    return render(request,'services.html')    
def services2(request):
    #return   HttpResponse('This is service page')
    return render(request,'services2.html')        
def contacts(request):
    #return   HttpResponse('This is contact page')
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contacts = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contacts.save()
        messages.success(request, 'Submitted succesfully! ')



    return render(request,'contacts.html')    


    #N0TE = if we chabnge anythingin a program we have to again run makemigrations and migrate cmd
    #n order to update it inside database
