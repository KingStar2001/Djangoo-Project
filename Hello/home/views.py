from django.shortcuts import render, HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")
    messages.success(request, 'Welcome!')
    return render(request , 'index.html')
def about(request):
    # return HttpResponse("This is about page")
    return render(request , 'about.html')
def services(request):
    # return HttpResponse("This is services page")
    return render(request , 'services.html')
def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent!")
    return render(request , 'contact.html')