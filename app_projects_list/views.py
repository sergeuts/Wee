from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


def index(request):
    # return HttpResponse("<h1>Страница приложения Wee.</h1>")
    # return render(request, 'pl/index.html', {'title': 'Мой title'})
    def table_n_recs(model_name):
        recs = model_name.objects.all()
        s = str(recs.model)
        model_name = s[s.find('models') + 7:-2]
        return {'name': model_name, 'recs': recs}

    tables = ([
        table_n_recs(Purposes),
        table_n_recs(Skills),
        table_n_recs(Availability),
        table_n_recs(TypeOfContacts),
        table_n_recs(Industries),
        table_n_recs(StagesOfStartup)])

    links = [{'name': 'About us', 'url': 'about_us'},
             {'name': 'Privacy policy', 'url': 'privacy_policy'},
             {'name': 'Cookie policy', 'url': 'cookie_policy'},
             {'name': 'Terms of service', 'url': 'terms_of_service'}]
    return render(request, 'pl/index.html', {'links': links, 'tables': tables})

def privacy_policy(request):
    return render(request, 'pl/privacy_policy.html')


def cookie_policy(request):
    return render(request, 'pl/cookie_policy.html')


def terms_of_service(request):
    return render(request, 'pl/terms_of_service.html')


def about_us(request):
    return render(request, 'pl/about_us.html')