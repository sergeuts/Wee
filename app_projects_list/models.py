from django.db import models
import datetime
from sys import argv


class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    first_name = models.CharField(blank=True, max_length=255, verbose_name="First name")
    last_name = models.CharField(blank=True, max_length=255, verbose_name="Last name")
    nick_name = models.CharField(blank=True, max_length=255, verbose_name="Nick name")
    email = models.EmailField(blank=True, verbose_name="Email")  # unique=True,
    company_name = models.CharField(blank=True, max_length=255, verbose_name="Company name")
    location = models.CharField(blank=True, max_length=255, verbose_name="Address")
    country = models.CharField(max_length=255, blank=True, verbose_name="Country")
    state = models.CharField(max_length=255, blank=True, verbose_name="State")
    city = models.CharField(max_length=255, blank=True, verbose_name="City")
    birthday_date = models.DateTimeField(blank=True, null=True, verbose_name="Birthday date")
    gender = models.ForeignKey('Gender', blank=True, on_delete=models.PROTECT)
    portfolio = models.TextField(blank=True, verbose_name="portfolio")
    presentation = models.TextField(blank=True, verbose_name="Presentation")
    education = models.TextField(blank=True, verbose_name="Education")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")
    deleted_date = models.DateTimeField(null=True, verbose_name="Deleted date")
    #joined_date = models.DateTimeField(default=datetime.date.today, verbose_name="Joined date ")
    user_rights = models.ForeignKey('UserRights', null=True, on_delete=models.PROTECT, verbose_name="User rights")
    source = models.ForeignKey('Sources', blank=True, null=True, on_delete=models.PROTECT, verbose_name="Source")
    rating = models.IntegerField(blank=True, verbose_name="Ratings")
    s_id = models.CharField(blank=True, max_length=25, verbose_name="Source id")
    web_site = models.SlugField(blank=True, max_length=255, db_index=True, verbose_name="Web site")
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    documents_copy = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Documents")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    is_premium_user = models.BooleanField(default=False, verbose_name="Premium user")

    # preferred_method_of_communication    # work_schedule: flexible schedule, full-time, shift schedule, shift method, remote work
    # class EmailField(max_length=254, **options)
    # class FileField(upload_to='', storage=None, max_length=100, **options)
    # class IntegerField(**options)

    def __str__(self):
        return self.name

    def absolute_url(self):
        return reverse('index')

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Author")
    web_site = models.SlugField(blank=True, max_length=255, null=True, db_index=True, verbose_name="Web site")
    why_are_you_good = models.TextField(blank=True, verbose_name="Why you would make a good co-founder")
    description = models.TextField(blank=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    # in the development, in working
    registration_date = models.DateTimeField(default=datetime.date.today, verbose_name="Registration date")
    end_date = models.DateTimeField(null=True, verbose_name="Deadline (closing) date")
    purpose = models.ForeignKey('Purposes', blank=True, null=True, on_delete=models.PROTECT,
                                verbose_name="Main purpose")  # on_delete=models.SET_NULL(collector=),
    industry = models.ForeignKey('Industries', blank=True, null=True, on_delete=models.PROTECT, verbose_name="Source")
    your_skills = models.TextField(blank=True, verbose_name="Your skills")
    skills_you_are_looking = models.TextField(blank=True, verbose_name="Skills you are looking")
    # your_skills = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Your skills")
    # skills_you_are_looking = models.ForeignKey('Skills', on_delete=models.PROTECT,
    #                                            verbose_name="Skills you are looking")
    availability = models.ForeignKey('Availability', default=1, blank=True, null=True, on_delete=models.PROTECT,
                                     verbose_name="Availability")
    startup_stage = models.ForeignKey('StagesOfStartup', null=True, on_delete=models.PROTECT, verbose_name="Stages of startup")
    documents = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Documents about project")
    source = models.ForeignKey('Sources', blank=True, null=True, on_delete=models.RESTRICT, verbose_name="Source")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'


class SkillsInProjects(models.Model):  # CompetenciesInProjects
    project = models.ForeignKey('Projects', on_delete=models.PROTECT, verbose_name="Project")
    skills = models.ForeignKey('Skills', on_delete=models.PROTECT, verbose_name="Skills")

    def __str__(self):
        return self.name


class Sources(models.Model):  # referral link,  source of customer engagement
    name = models.CharField(max_length=255, verbose_name="Name")
    link = models.CharField(max_length=255, verbose_name="Link")
    link_template = models.CharField(max_length=255, verbose_name="Link template")

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


class Gender(models.Model):
    name = models.CharField(max_length=6, verbose_name="Name")

    def __str__(self):
        return self.name


# def get_address(s):
#     city, state, country = '', '', ''
#     s = [*map(str.strip, s.split(','))]
#     if len(s) == 3:
#         city, state, country = s
#     elif len(s) == 2:
#         city, country = s
#     elif len(s) == 1:
#         if '-' in s[0]:
#             s = s[0].split()
#             if len(s) == 2:
#                 city, country = s
#         else:
#             country = s[0]
#     return city, state, country
#
# def load_tables():
#     from pickle import load
#     with open(r"C:\it\Projects\WeeDeal\parse\pickle.txt", 'rb') as file:
#         table = load(file)
#     # Users name country state city presentation photo source web_site
#     # Projects - name user why_are_you_good description purpose your_skills skills_you_are_looking availability stages_of_startup
#     # 'name	location	rating	why you are good	description	startup_stage	industry	availability	website	your skills	skills needed	id	pro user'
#     for rec in table:
#         city, state, country = get_address(rec.location)
#         proj_fields = {
#             'name': rec.name,
#             'user': user.id,
#             'why_are_you_good': rec.why_are_you_good,
#             'description': rec.description,
#             'your_skills': rec.your_skills,
#             'skills_you_are_looking': rec.skills_you_are_looking,
#             'stages_of_startup': rec.stages_of_startup,
#             'availability': rec.availability,
#             'source': source,
#         }
#
#
#         user_fields = {
#             'name': rec.name,
#             'location': rec.location,
#             'city': rec.city,
#             'state': rec.state,
#             'country': rec.country,
#             'rating': rec.rating,
#             'web_site': rec.web_site,
#             's_id': rec.id,
#             'source': source,
#             'premium': rec.id
#         }
#
#         user = Users.objects.create(fields)
#         user.save()
#
#
#
# def clear_tables():
#     pass


def fill_table(table, values):
    if not table.objects.all().count():
        for n in values:
            r = table.objects.create(name=n)
            r.save()


def init_system_tables():
    fill_table(Gender, ['Male', 'Female'])

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

    fill_table(UserRights, ['ordinary', 'privileged', 'full'])

    industries = ('Finance/Fintech,  Retail,  E-Commerce,  Construction/Trade,  '
                  'Agency - digital (eg. Marketing, Web Design),  '
                  'Agency - other (eg. Real Estate, Recruitment),  '
                  'Consulting,  Manufacturing,  Wholesale,  Web or Mobile app,  '
                  'Website (eg. news, affiliate),  Other').split(',  ')
    fill_table(Industries, industries)
    # https://www.angelinvestmentnetwork.us/
    industries = ['Agriculture', 'Business Services', 'Education & Training', 'Energy & Natural Resources',
                  'Entertainment & Leisure', 'Fashion & Beauty', 'Finance', 'Food & Beverage',
                  'Hospitality, Restaurants & Bars',
                  'Manufacturing & Engineering', 'Media', 'Medical & Sciences', 'Personal Services',
                  'Products & Inventions',
                  'Property ', 'Retail', 'Sales & Marketing', 'Software', 'Technology', 'Transportation']

    # kickstarter.com
    # Arts
    # Comics & Illustration
    # Design & Tech
    # Film
    # Food & Craft
    # Games
    # Music
    # Publishing

    stages_of_startup = ('Validation - Concept exploration & research, '
                         'Planning - Business model & business plan writing, '
                         'Building - Product building or service being setup, '
                         'Launched - Existing clients or customers').split(', ')
    fill_table(StagesOfStartup, stages_of_startup)


shell_commands = '''

python manage.py createsuperuser
python manage.py shell
from app_projects_list.models import *
init_system_tables()
recs = Purposes.objects.all()
s = str(recs.model)
model_name = s[s.find('models')+7:-2]
quit()
'''

if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1] == 'load_table':
            load_tables()
