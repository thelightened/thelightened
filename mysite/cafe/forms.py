#!/usr/bin/env python
# coding=utf-8
from django.contrib.auth.models import User
from django import forms

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
    first_name = forms.CharField(min_length=2,max_length=18, )
      
       
    last_name = forms.CharField(min_length=1,max_length=18,)
      
    widget=forms.TextInput(attrs={'class': 'form-control'})
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()