#!/usr/bin/env python
# coding=utf-8
from django.contrib.auth.models import User
from django import forms
from django.forms.extras import widgets

def get(self, request):
    form = PersonDetailsForm()
    return render(request, self.template_name, {'class': 'form-control'})

    def post(self, request):
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            return redirect('index/')
        else:
            return render(request, self.template_name, {'class': 'form-control'})


class SignupForm(forms.Form):

    last_name = forms.CharField(label=("姓氏"),min_length=1,max_length=18,)
    first_name = forms.CharField(label=("名字"),min_length=2,max_length=18, )
    birth_date = forms.DateField(label=("生日"),widget=widgets.SelectDateWidget(years=range(1900, 2100))) 

    widget=forms.TextInput(attrs={'class': 'form-control'})
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birth_date']
        user.email = self.cleaned_data['email']
        user.save()