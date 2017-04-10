#!/usr/bin/env python
# coding=utf-8
from django.contrib.auth.models import User
from django import forms
# from allauth.account.forms import LoginForm

# class RegisterForm(forms.Form):
#     username = forms.CharField(
#         label=u'暱稱',
#         help_text=u'暱稱可用於登入，不可包含空格和@字元。',
#         max_length=20,
#         initial='Nickname',
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         )
#     label=u'Email',
#     help_text=u'Email可用於登入，且需要Email来找回密碼，所以請輸入您正在使用的Email。',

#     email = forms.EmailField(
#         max_length=50,
#         initial='acdefg@gmail.com',
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         )

#     password = forms.CharField(
#         label=u'密碼',
#         help_text=u'密碼只有長度要求，長度為 6 ~ 18 。',
#         min_length=6,
#         max_length=18,
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         )

#     confirm_password = forms.CharField(
#         label=u'確認密碼',
#         min_length=6,
#         max_length=18,
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         )

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if ' ' in username or '@' in username:
#             raise forms.ValidationError(u'暱稱中不能包含空格和@字元')
#         res = User.objects.filter(username=username)
#         if len(res) != 0:
#             raise forms.ValidationError(u'此暱稱已被使用，請重新輸入')
#         return username

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         res = User.objects.filter(email=email)
#         if len(res) != 0:
#             raise forms.ValidationError(u'此Email已經註冊過，請重新輸入')
#         return email

#     def save(self):
#         username = self.cleaned_data['username']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#         user = User.objects.create_user(username, email, password)
#         user.save()

#     def clean(self):
#         cleaned_data = super(RegisterForm, self).clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if password and confirm_password:
#             if password != confirm_password:
#                 raise forms.ValidationError(u'兩次密碼输入不一致，請重新輸入')
def get(self, request):
    form = PersonDetailsForm()
    return render(request, self.template_name, {'class': 'form-control'})

    def post(self, request):
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            return redirect('index/')
        else:
            return render(request, self.template_name, {'class': 'form-control'})
class LoginForm(forms.Form):
    username = forms.CharField(label=u'暱稱',
     initial='Nickname',
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # email = forms.CharField(
    #     max_length=50,
    #     initial='acdefg@gmail.com',
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     )

    password = forms.CharField(label=u'密碼',
        
        min_length=3,
        max_length=18,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# class RegisterForm(forms.Form):
#     username = forms.CharField(label=u'暱稱',
       
#         max_length=20,
        
#         widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # def __init__(self, *args, **kwargs):
#     #     super(MyForm, self).__init__(*args, **kwargs)
#     #     self.fields['myfield'].widget.attrs.update({'class' : 'form-control'})

#     email = forms.EmailField(
#         max_length=50,
      
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         )



#     password = forms.CharField(label=u'密碼',
        
#         min_length=3,
#         max_length=18,
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     password_check = forms.CharField(label=u'密碼確認',
        
#         min_length=3,
#         max_length=18,
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignupForm(forms.Form):
    first_name = forms.CharField(min_length=2,max_length=18, )
      
       
    last_name = forms.CharField(min_length=1,max_length=18,)
      
    widget=forms.TextInput(attrs={'class': 'form-control'})
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()