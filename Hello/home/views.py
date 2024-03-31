from django.shortcuts import render, HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")
    # messages.success(request, 'Welcome!')
    return render(request , 'index.html')
def about(request):
    # return HttpResponse("This is about page")
    return render(request , 'about.html')
def services(request):
    # return HttpResponse("This is services page")
    return render(request , 'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        projects = request.POST.get('projects')
        experience = request.POST.get('experience')
        resume = request.FILES.get('resume')
        photos = request.FILES.get('photos')
        
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            projects=projects,
            experience=experience,
            resume=resume,
            photos=photos,
            date=datetime.today()
        )
        contact.save()
        
        messages.success(request, "Your Message has been sent!")
        
        # Send email
        send_mail(
            f'Contact Form Submission: {subject}',
            f'Name: {name}\nEmail: {email}\nMessage: {message}\nProjects: {projects}\nExperience: {experience}',
            email,  # Use the user-provided email address as the sender's email address
            ['kingstar09122001@gmail.com'],  # Receiver's email address
            fail_silently=False,
        )

        return HttpResponseRedirect('/razorpay')  # Redirect to the Razorpay page after successful form submission
    else:
        return render(request , 'contact.html')
    
def static(request):
    return render(request , 'static.html')
def custom(request):
    return render(request , 'custom.html')
def temp1(request):
    return render(request , 'temp1.html')
def temp2(request):
    return render(request , 'temp2.html')
def temp3(request):
    return render(request , 'temp3.html')
def temp4(request):
    return render(request , 'temp4.html')
def temp5(request):
    return render(request , 'temp5.html')
def temp6(request):
    return render(request , 'temp6.html')
def temp7(request):
    return render(request , 'temp7.html')
def temp8(request):
    return render(request , 'temp8.html')
def temp9(request):
    return render(request , 'temp9.html')
def razorpay(request):
    return render(request , 'razorpay.html')


