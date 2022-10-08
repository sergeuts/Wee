from django.db import models
import datetime

class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(max_length=255, verbose_name="Last name")
    nick_name = models.CharField(max_length=255, verbose_name="Nick name")
    company_name = models.CharField(max_length=255, verbose_name="Company name")
    Country = models.CharField(max_length=255, verbose_name="Country")
    State = models.CharField(max_length=255, verbose_name="State")
    City = models.CharField(max_length=255, verbose_name="City")
    portfolio = models.TextField(blank=True, verbose_name="portfolio")
    presentation = models.TextField(blank=True, verbose_name="Presentation")
    education = models.TextField(blank=True, verbose_name="Education")
    registration_date = models.DateTimeField(default=datetime.date.today, auto_now=True, verbose_name="Registration date")
    user_rights = models.ForeignKey('UserRights', on_delete=models.PROTECT, verbose_name="User rights")
    ratings = models.IntegerField(verbose_name="Ratings")
    web_site = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Web site")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    documents_copy = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Documents")
    is_disabled = models.BooleanField(default=True, verbose_name="Disabled")
    is_deleted = models.BooleanField(default=True, verbose_name="Deleted")
    main_purpose = models.ForeignKey('Purposes', on_delete=models.PROTECT, verbose_name="Main purpose")
    main_skill = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Basic skills")
    availability = models.ForeignKey('Availability', on_delete=models.PROTECT, verbose_name="Availability")
    stages_of_startup = models.ForeignKey('StagesOfStartup', on_delete=models.PROTECT, verbose_name="Stages of startup")
    #preferred_method_of_communication
    #work_schedule: flexible schedule, full-time, shift schedule, shift method, remote work
    #class EmailField(max_length=254, **options)
    # class FileField(upload_to='', storage=None, max_length=100, **options)
    # class IntegerField(**options)

class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Author")
    description = models.TextField(blank=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    # in the development, in working
    registration_date = models.DateTimeField(default=datetime.date.today, auto_now=True, verbose_name="Registration date")
    end_date = models.DateTimeField(default=datetime.date.today, auto_now=True, verbose_name="Deadline (closing) date")


class SkillsInProjects(models.Model):  # CompetenciesInProjects
    project = models.ForeignKey('Projects', on_delete=models.PROTECT, verbose_name="Project")
    skills = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Skills")


class UserRights(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

class Purposes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

predefined_purposes = ("Looking to partner with someone else's idea, "
                       'Has an idea for a startup, '
                       "I have my own ideas, but I'm also looking for ideas from others")

class Skills(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

predefined_skills = 'Developer, Designer, Marketer, Business Development Manager, Sales Manager, Product Manager'\

class Availability(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")

# Availability (Hours per week available to commit)
predefined_availability = '0-10 hours per week, 10-20 hours per week, 20-30 hours per week, 30+ hours per week'

class TypeOfContacts(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

predefined_type_of_contacts = 'Phone, Email, Linkedin, Instagram, Facebook, WhatsApp, Telegram, Others'

class Industries(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

predefined_industries = ('Finance/Fintech, Retail, E-Commerce, Construction/Trade, ' 
                        'Agency - digital (eg. Marketing, Web Design), Agency - other (eg. Real Estate, Recruitment), '  
                        'Consulting, Manufacturing, Wholesale, Web or Mobile app, Website (eg. news, affiliate), Other')

class StagesOfStartup(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")

predefined_stages_of_startup = ('Validation - Concept exploration & research, '
                                'Planning - Business model & business plan writing, '
                                'Building - Product building or service being setup, '
                                'Launched - Existing clients or customers')
