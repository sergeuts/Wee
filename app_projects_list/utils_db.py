# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wee.settings')

# import django
# django.setup()
# from app.models import MyClass;


# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
# from Wee.wsgi import *
from app_projects_list.models import *
from sys import argv


# не помогло Error: Requested setting INSTALLED_APPS, but settings are not configured.
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', r'C:\it\Projects\WeeDeal\Wee\Wee\settings.py')
# set DJANGO_SETTINGS_MODULE= C:\it\Projects\WeeDeal\Wee\Wee\settings.py

def get_address(s):
    city, state, country = '', '', ''
    s = [*map(str.strip, s.split(','))]
    if len(s) == 3:
        city, state, country = s
    elif len(s) == 2:
        city, country = s
    elif len(s) == 1:
        if '-' in s[0]:
            s = s[0].split()
            if len(s) == 2:
                city, country = s
        else:
            country = s[0]
    return city, state, country


def find_rec(table, values_dic):
    rr = table.objects.filter(**values_dic)
    if len(rr) == 1:
        return rr[0]
    elif not rr:  # len[rr] == 0:
        if 's_id' in values_dic:
            return
        print(f'Records in table "{table.__name__}" with filter {values_dic} not found')
    else:
        print(f'Found {len(rr)} records in table "{table.__name__}" with filter {values_dic}')
        print(f'id \t name')
        for r in rr:
            print(f'{r.id} \t {r.name}')


def load_tables_from_sh():
    from pickle import load
    # with open(r"C:\it\Projects\WeeDeal\parse\pickle.txt", 'rb') as file: table = load(file)
    with open(r"C:\it\Projects\WeeDeal\parse\pickle.txt", 'rb') as file:
        table = load(file)
    # Users name country state city presentation photo source web_site
    # Projects - name user why_are_you_good description purpose your_skills skills_you_are_looking availability stages_of_startup
    # 'name	location	rating	why you are good	description	startup_stage	industry	availability	website	your skills	skills needed	id	pro user'
    # rec = table[0]
    replaces = {'Finance/ Fintech': 'Finance/Fintech', 'Website (eg news, affiliate)': 'Website (eg. news, affiliate)'}
    v_user_rights = find_rec(UserRights, {'name': 'ordinary'})
    v_source = find_rec(Sources, {'name': 'sh'})
    v_gender = find_rec(Gender, {'name': 'Female'})
    for rec in table:
        if rec[6] in replaces:
            rec[6] = replaces[rec[6]]
        print(rec[0])
        city, state, country = get_address(rec[1])
        user_fields = {
            'name': rec[0],
            'location': rec[1],
            'city': city,
            'state': state,
            'country': country,
            'rating': rec[2],
            'web_site': rec[8],
            's_id': rec[11],
            'gender': v_gender,
            'source': v_source,
            'is_premium_user': rec[12],
            'user_rights': v_user_rights,
        }
        # user = None
        user = find_rec(Users, {'s_id': rec[11]})
        if user is None:
            user = Users.objects.create(**user_fields)
            user.save()

        proj_fields = {
            'name': rec[0],
            'user': user,
            'why_are_you_good': rec[3],
            'description': rec[4],
            'stages_of_startup': find_rec(StagesOfStartup, {'name': rec[5]}),
            'industry': find_rec(Industries, {'name': rec[6]}),
            'availability': find_rec(Availability, {'name': rec[7]}),
            'web_site': rec[8],
            'your_skills': rec[9],
            'skills_you_are_looking': rec[10],
            'source': Sources.objects.first(),
        }
        proj = Projects.objects.create(**proj_fields)
        proj.save()


def clear_tables():
    pass


def get_row_value(row, fields):
    res = {}
    # for f in fields:
    #     value = row.__getattribute__(f)
    #     if '.models.' in str(type(value)):
    #         value = value.name
    #     res[f] = value

    for f in fields:
        value = row
        for f in fields:
            ff = f.split('.')
            nesting = len(ff)
            value = row
            for i in range(nesting):
                value = value.__getattribute__(ff[i])
            if '.models.' in str(type(value)):
                value = value.name
            res[f.replace('.', '_') if '.' in f else f] = value
    return res


def get_table_values(table, filter=None, fields=None):
    if filter:
        rr = table.objects.filter(**filter)
    else:
        rr = table.objects.all()
    return [get_row_value(row, fields) for row in rr]


# fields = ['name', 'startup_stage', 'web_site', 'industry', 'why_are_you_good', 'description', 'your_skills', 'skills_you_are_looking', 'availability']

if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1] == 'load_table':
            load_tables()
'''
from os import chdir
chdir(r'C:\it\Projects\WeeDeal\Wee')


import importlib
import app_projects_list.models
from app_projects_list.models import *
from app_projects_list.utils_db import get_address, Gender, Sources, Users, Projects
from pickle import load
with open(r"C:\it\Projects\WeeDeal\parse\pickle.txt", 'rb') as file: table = load(file)
rec = table[0]
city, state, country = get_address(rec[1])
user_fields = {}
user = Users.objects.create(**user_fields)
user.save()

importlib.reload(app_projects_list.models)

load_tables_from_sh()
Projects.objects.all().delete()
Users.objects.all().delete()
'''
