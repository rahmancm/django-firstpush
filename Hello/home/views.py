from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request,'index.html')
    #return HttpResponse("This is Home page")

def about(request):
    return render (request,'about.html')

def services(request):
    return render (request,'services.html')   

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        descp=request.POST.get('descp')
        contact=Contact(name=name, email=email,phone=phone,descp=descp,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Query has been sent.')
    return render (request,'contact.html')