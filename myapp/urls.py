
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("", views.home, name='home'), 
    path("home", views.home, name='home'),
    path("link", views.link, name="link"),
    path('add', views.add, name="add"),
    path("register", views.register, name='register'), 
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path('appointment',views.appointment, name='appointment'),
    path('patient',views.patient, name='patient'),
    path('history',views.history, name='history'),
    path('doctor',views.doctor,name='doctor'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('covid',views.covid,name='covid')
]
urlpatterns += staticfiles_urlpatterns()