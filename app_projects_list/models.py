from django.db import models
import datetime


class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    first_name = models.CharField(blank=True, max_length=255, verbose_name="First name")
    last_name = models.CharField(blank=True, max_length=255, verbose_name="Last name")
    nick_name = models.CharField(blank=True, max_length=255, verbose_name="Nick name")
    company_name = models.CharField(blank=True, max_length=255, verbose_name="Company name")
    Country = models.CharField(max_length=255, verbose_name="Country")
    State = models.CharField(max_length=255, verbose_name="State")
    City = models.CharField(max_length=255, verbose_name="City")
    portfolio = models.TextField(blank=True, verbose_name="portfolio")
    presentation = models.TextField(blank=True, verbose_name="Presentation")
    education = models.TextField(blank=True, verbose_name="Education")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")
    user_rights = models.ForeignKey('UserRights', blank=True, on_delete=models.PROTECT, verbose_name="User rights")
    ratings = models.IntegerField(blank=True, verbose_name="Ratings")
    web_site = models.SlugField(blank=True, max_length=255, unique=True, db_index=True, verbose_name="Web site")
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    documents_copy = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Documents")
    is_disabled = models.BooleanField(default=False, verbose_name="Disabled")
    is_deleted = models.BooleanField(default=False, verbose_name="Deleted")
    main_purpose = models.ForeignKey('Purposes', on_delete=models.PROTECT, verbose_name="Main purpose")
    main_skill = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Basic skills")
    availability = models.ForeignKey('Availability', on_delete=models.PROTECT, verbose_name="Availability")
    stages_of_startup = models.ForeignKey('StagesOfStartup', on_delete=models.PROTECT, verbose_name="Stages of startup")
    # preferred_method_of_communication
    # work_schedule: flexible schedule, full-time, shift schedule, shift method, remote work
    # class EmailField(max_length=254, **options)
    # class FileField(upload_to='', storage=None, max_length=100, **options)
    # class IntegerField(**options)

    def __str__(self):
        return self.name

    def absolute_url(self):
        return reverse('index')


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Author")
    description = models.TextField(blank=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    # in the development, in working
    registration_date = models.DateTimeField(default=datetime.date.today, verbose_name="Registration date")
    end_date = models.DateTimeField(default=datetime.date.today, verbose_name="Deadline (closing) date")

    def __str__(self):
        return self.name

class SkillsInProjects(models.Model):  # CompetenciesInProjects
    project = models.ForeignKey('Projects', on_delete=models.PROTECT, verbose_name="Project")
    skills = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Skills")

    def __str__(self):
        return self.name

class UserRights(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

class Purposes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

class Availability(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")

    def __str__(self):
        return self.name

class TypeOfContacts(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

    def __str__(self):
        return self.name

class Industries(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

    def __str__(self):
        return self.name

class StagesOfStartup(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

    def __str__(self):
        return self.name

def fill_table(table, values):
    if not table.objects.all().count():
        for n in values:
            r = table.objects.create(name=n)
            r.save()


def init_system_tables():
    purposes = ("Looking to partner with someone else's idea  "
                "Has an idea for a startup  "
                "I have my own ideas, but I'm also looking for ideas from others").split('  ')
    fill_table(Purposes, purposes)

    skills = 'Developer, Designer, Marketer, Business Development Manager, ' \
             'Sales Manager, Product Manager'.split(', ')
    fill_table(Skills, skills)

    # Availability (Hours per week available to commit)
    availability = '0-10 hours per week, 10-20 hours per week, ' \
                   '20-30 hours per week, 30+ hours per week'.split(', ')
    fill_table(Availability, availability)

    type_of_contacts = 'Phone, Email, Linkedin, Instagram, Facebook, ' \
                       'WhatsApp, Telegram, Others'.split(', ')
    fill_table(TypeOfContacts, type_of_contacts)

    industries = ('Finance/Fintech,  Retail,  E-Commerce,  Construction/Trade,  '
                  'Agency - digital (eg. Marketing, Web Design),  '
                  'Agency - other (eg. Real Estate, Recruitment),  '
                  'Consulting,  Manufacturing,  Wholesale,  Web or Mobile app,  '
                  'Website (eg. news, affiliate),  Other').split(',  ')
    fill_table(Industries, industries)

    stages_of_startup = ('Validation - Concept exploration & research, '
                         'Planning - Business model & business plan writing, '
                         'Building - Product building or service being setup, '
                         'Launched - Existing clients or customers').split(', ')
    fill_table(StagesOfStartup, stages_of_startup)


shell_commands = '''

python manage.py shell
from app_projects_list.models import *
recs = Purposes.objects.all()
s = str(recs.model)
model_name = s[s.find('models')+7:-2]
'''
