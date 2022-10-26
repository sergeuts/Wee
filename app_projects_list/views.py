from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *

#import mimetypes
#mimetypes.add_type("text/css", ".css", True)

def select(request):
    from app_projects_list.utils_db import get_table_values
    print('Helo')

def index(request):
    from app_projects_list.utils_db import get_table_values

    search_string = {}
    if request.method == 'POST':
        form = FilterForm(request.POST)
        for field,value in request.POST.items():
            if field in ['name', 'web_site', 'description', 'your_skills', 'skills_you_are_looking', 'why_are_you_good',
                         'description', 'your_skills', 'skills_you_are_looking',] and value:
                search_string[field + '__contains'] = value
            elif field in ['startup_stage', 'industry', 'availability'] and value:
                search_string[field] = value
    # if form.is_valid():
        #     #print(form.cleaned_data)
        #     try:
        #         Projects.objects.create(**form.cleaned_data)
        #         return redirect('home')
        #     except:
        #         form.add_error(None, 'Error creating record')
    else:
        form = FilterForm()
    #recs = Projects.objects.all()
    fields = ['name', 'user', 'user.location', 'startup_stage', 'web_site', 'industry', 'why_are_you_good', 'description', 'your_skills',
              'skills_you_are_looking', 'availability']
    table = get_table_values(Projects, filter=search_string, fields=fields)
    return render(request, 'pl/index.html', {'table': table, 'quantity': len(table), 'form': form})


def index2(request):
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
    return render(request, 'pl/index2.html', {'links': links, 'tables': tables})

def privacy_policy(request):
    return render(request, 'pl/privacy_policy.html')


def cookie_policy(request):
    return render(request, 'pl/cookie_policy.html')

def main(request):
    return render(request, 'pl/main.css')

def terms_of_service(request):
    return render(request, 'pl/terms_of_service.html')


def about_us(request):
    return render(request, 'pl/about_us.html')