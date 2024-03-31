from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("static", views.static, name='static'),
    path("custom", views.custom, name='custom'),
    path("temp1", views.temp1, name='temp1'),
    path("temp2", views.temp2, name='temp2'),
    path("temp3", views.temp3, name='temp3'),
    path("temp4", views.temp4, name='temp4'),
    path("temp5", views.temp5, name='temp5'),
    path("temp6", views.temp6, name='temp6'),
    path("temp7", views.temp7, name='temp7'),
    path("temp8", views.temp8, name='temp8'),
    path("temp9", views.temp9, name='temp9'),
    path("razorpay",views.razorpay, name='razorpay'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)