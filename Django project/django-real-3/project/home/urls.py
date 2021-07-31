from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('services', views.index, name = 'services'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('android', views.android, name = 'android'),
    path('signup', views.handlesignup, name = 'handlesignup'),
    path('logout', views.handlesLogout, name = 'handlesLogout'),
    path('login', views.handlesLogin, name = 'handlesLogin'),
    

    

 

]



