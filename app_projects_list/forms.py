from django import forms
from django.core.exceptions import ValidationError
from .models import *


class FilterForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name', required=False)
    web_site = forms.SlugField(max_length=255, label="Web site", required=False)
    startup_stage = forms.ModelChoiceField(queryset=StagesOfStartup.objects.all(), label="Startup stage",
                                           empty_label="", required=False)
    industry = forms.ModelChoiceField(queryset=Industries.objects.all(), label="Industry",
                                      empty_label="", required=False)
    availability = forms.ModelChoiceField(queryset=Availability.objects.all(), label="Availability",
                                          empty_label="", required=False)
    why_are_you_good = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}), label="Why you are good", required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}), label="Description", required=False)
    your_skills = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}), label="Your skills", required=False)
    skills_you_are_looking = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}),
                                             label="Skills needed", required=False)
    #is_active = forms.BooleanField(label="Active", required=False, initial=True)
