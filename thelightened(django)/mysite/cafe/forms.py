#!/usr/bin/env python
# coding=utf-8
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        label=u'暱稱',
        help_text=u'暱稱可用於登陸，不能包含空格和@字符。',
        max_length=20,
        initial='',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        )

    email = forms.EmailField(
        label=u'Email',
        help_text=u'Email可用於登陸，最重要的是需要Email来找回密码，所以請輸入您可使用的Email。',
        max_length=50,
        initial='',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        )

    password = forms.CharField(
        label=u'密碼',
        help_text=u'密碼只有長度要求，長度為 6 ~ 18 。',
        min_length=6,
        max_length=18,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        )

    confirm_password = forms.CharField(
        label=u'確認密碼',
        min_length=6,
        max_length=18,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username or '@' in username:
            raise forms.ValidationError(u'暱稱中不能包含空格和@字符')
        res = User.objects.filter(username=username)
        if len(res) != 0:
            raise forms.ValidationError(u'此暱稱已被使用，請重新輸入')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        res = User.objects.filter(email=email)
        if len(res) != 0:
            raise forms.ValidationError(u'此Email已经註冊過，請重新輸入')
        return email

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        user.save()

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(u'兩次密碼输入不一致，請重新輸入')

    def get(self, request):
        form = PersonDetailsForm()
        return render(request, self.template_name, {'class': 'form-control'})
    def post(self, request):
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            return redirect('index/')
        else:
            return render(request, self.template_name, {'class': 'form-control'})

    