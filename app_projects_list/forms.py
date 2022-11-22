from django import forms
from django.core.exceptions import ValidationError
from .models import *


class FilterForm(forms.Form):
    # name = forms.CharField(max_length=255, label='Name', required=False)
    web_site = forms.SlugField(max_length=255, label="Web site", required=False)
    location = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}), label="Location", required=False)
    startup_stage = forms.ModelChoiceField(queryset=StagesOfStartup.objects.all(), label="Startup stage",
                                           empty_label="", required=False)
    industry = forms.ModelChoiceField(queryset=Industries.objects.all(), label="Industry",
                                      empty_label="", required=False)
    availability = forms.ModelChoiceField(queryset=Availability.objects.all(), label="Availability",
                                          empty_label="", required=False)
    why_are_you_good = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}), label="About founder", required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}), label="Description", required=False)
    your_skills = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}), label="Your skills", required=False)
    skills_you_are_looking = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}),
                                             label="Skills needed", required=False)
    number_of_columns = forms.IntegerField(label="Number of columns", initial=3, required=False)
    show_all_fields = forms.BooleanField(label="Show all fields", required=False)
    #is_active = forms.BooleanField(label="Active", required=False, initial=True)
