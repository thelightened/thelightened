from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from . import models
from django.contrib import auth
from django.template import RequestContext
from django.conf.urls import  url
from django.views import generic

from django.core.urlresolvers import reverse_lazy 
from django.views.generic.edit import FormView 
from django.contrib.auth import authenticate, login as auth_login
# from forms import RegisterForm  
from cafe import forms
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage

from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.account.forms import LoginForm
from django.contrib.auth import authenticate, login
from allauth.account.adapter import DefaultAccountAdapter



class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog.html"
    paginate_by = 6


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"


def index(request, pid=None, del_pass=None):
    index = models.IndexImage.objects.all()
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)



def test(request):
	return render_to_response('test.html')
	
def coffeebeans(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('coffeebeans.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def blog(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('blog.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def product(request):
	return render_to_response('product.html')

def about(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
	messages.get_messages(request)
    template = get_template('about.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)
    # return render_to_response('about.html')

def partnershop(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('partnershop.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def cart(request):
     if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
     messages.get_messages(request)
     template = get_template('cart.html')
     request_context = RequestContext(request)
     request_context.push(locals())
     html = template.render(request_context)
     return HttpResponse(html)
     # return render_to_response('cart.html')



def article(request):
    return render_to_response('article.html')    

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "logout success")
    return redirect('/index')




# def account(request):
#     if request.method == 'POST':
#         login_form = forms.LoginForm(request.POST)
#         if login_form.is_valid():
#             login_name=request.POST['username'].strip()
#             login_password=request.POST['password']
#             user = authenticate(username=login_name, password=login_password)
#             if user is not None:
#                 if user.is_active:
#                     auth.login(request, user)
#                     messages.add_message(request, messages.SUCCESS, 'successful')
#                     return redirect('/index')
#                 else:
#                     messages.add_message(request, messages.WARNING, 'wrong password, please check again!')
#             else:
#                 messages.add_message(request, messages.WARNING, 'It can not login now!')
#         else:
#             messages.add_message(request, messages.INFO,'please check the column info')
#     else:
#         login_form = forms.LoginForm()

#     template = get_template('account.html')
#     request_context = RequestContext(request)
#     request_context.push(locals())
#     html = template.render(request_context)
#     return HttpResponse(html)


# def Login(request):
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             name=request.POST['username'].strip()
#             password=request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     messages.add_message(request, messages.SUCCESS, 'successful')
#                     return redirect('/index')
#                 else:
#                     messages.add_message(request, messages.WARNING, 'wrong password, please check again!')
#             else:
#                 messages.add_message(request, messages.WARNING, 'It can not login now!')
#         else:
#             messages.add_message(request, messages.INFO,'please check the column info')
#     else:
#         form = forms.LoginForm()

#     template = get_template('login.html')
#     request_context = RequestContext(request)
#     request_context.push(locals())
#     html = template.render(request_context)
#     return HttpResponse(html)

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.username = data['username']
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.gender = data['gender']
        user.birth_date = data['birth_date']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user


