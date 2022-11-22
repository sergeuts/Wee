from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *
from app_projects_list.utils_db import get_table_values


#import mimetypes
#mimetypes.add_type("text/css", ".css", True)


def select(request):
    from app_projects_list.utils_db import get_table_values
    print('Helo')


def home(request):
    fields = ['name', 'user', 'user.location', 'startup_stage', 'web_site', 'industry', 'your_skills',
              'skills_you_are_looking', 'availability']
    table = get_table_values(Projects, filter='', fields=fields)
    return render(request, 'pl/home.html', {'table': narezka(table[:9], 3), 'layout': 'default'})


def faq(request):
    return render(request, 'pl/FAQ.html', {})


def test(request):
    return render(request, 'pl' + request.path + '.html', {})


def projects(request):
    search_string = {}
    layout = {'number_of_columns': 3, 'show_all_fields': False}
    if request.method == 'POST':
        form = FilterForm(request.POST)
        for field,value in request.POST.items():
            if not value:
                continue
            if field in ['name', 'web_site', 'description', 'your_skills', 'skills_you_are_looking', 'why_are_you_good',
                         'description', 'your_skills', 'skills_you_are_looking', 'location']:
                if field in ['location']:
                    field = 'user__' + field
                search_string[field + '__contains'] = value
            elif field in ['startup_stage', 'industry', 'availability']:
                search_string[field] = value
            elif field in ['show_all_fields']: # checkbox
                layout[field] = True if form.data['show_all_fields'] == 'on' else False
            elif field in ['number_of_columns']:
                layout[field] = form.data['number_of_columns']
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
    fields = ['name', 'user', 'user.location', 'startup_stage', 'web_site', 'industry', 'your_skills',
              'skills_you_are_looking', 'availability']
    if layout['show_all_fields']:
        fields.extend(['why_are_you_good', 'description'])
    table = get_table_values(Projects, filter=search_string, fields=fields)
    return render(request, 'pl/projects.html', {'table': narezka(table, int(layout['number_of_columns'])), 'quantity': len(table), 'form': form, 'layout': layout})


def narezka(s, len1):
    return [s[i: i+len1] for i in range(0, len(s), len1)]


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

def login(request):
    return render(request, 'pl/login.html')