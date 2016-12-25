from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from . import models
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import patterns, url
from django.views import generic
class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

def index(request):

	index = models.IndexImage.objects.all()
	return render_to_response('index.html',RequestContext(request,locals()))



def test(request):
	return render_to_response('test.html')
	
def coffeebeans(request):
	return render_to_response('coffeebeans.html')

def blog(request):
	return render_to_response('blog.html')

def product(request):
	return render_to_response('product.html')

def about(request):
	return render_to_response('about.html')

def partnershop(request):
	return render_to_response('partnershop.html')

def logout(request):	
	auth.logout(request)
	return HttpResponseRedirect('/indexrequest/')

# def account(request):
# 	return render_to_response('account.html')

def account(request):

    if request.user.is_authenticated(): 
         auth.logout(request)
    	 return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('account.html') 


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/index/')
	else:
		form = UserCreationForm()
	return render_to_response('indexregister.html',RequestContext(request,locals()))


