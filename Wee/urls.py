"""Wee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_projects_list.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('m1', test, name='Скрывающееся левостороннее меню на Bootsrap 5'),
    path('m2', test, name='Скрывающееся меню сайта на HTML и CSS'),
    path('test_1', test, name='home page'),
    path('test_2', test, name='home page'),
    path('test_3', test, name='home page'),
    path('trust_satety_security', test, name='Trust, satety, security'),
    path('FAQ', faq, name='Whee-Launch projects'),
    path('home', home, name='Whee-Launch projects'),
    path('', home, name='Whee-Launch projects'),
    path('index', home, name='Whee-Launch projects'),
    path('projects', projects, name='Whee-Launch projects'),
    path('index2', index2, name='Whee-Launch projects'),
    path('privacy_policy', privacy_policy, name='Privacy policy'),
    path('cookie_policy', cookie_policy, name='Cookie policy'),
    path('terms_of_service', terms_of_service, name='Terms of service'),
    path('main.css', main, name='main'),
    path('login', login, name='About us'),
    path('about_us', about_us, name='About us'),
    path('select', select, name='Select'),
]
