from django.shortcuts import render,HttpResponse
from datetime import datetime
from hello.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    # return HttpResponse("this is about page")
    return render(request,"about.html")
def services(request):
    # return HttpResponse("this is services page")
    return render(request,"services.html")
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        phone=request.POST.get('phone')
        new_contact=Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        new_contact.save()
        messages.success(request, "your message has been sent")
    return render(request,"contact.html")