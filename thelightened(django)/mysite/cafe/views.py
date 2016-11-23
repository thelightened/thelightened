from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from cafe.models import IndexImage, MyModel
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm


def index(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/indexrequest/')

	username = request.POST.get('username','')
	password = request.POST.get('password','')

	user = auth.authenticate(username=username,password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/indexrequest/')
	else:
		return render_to_response('index.html',RequestContext(request,locals()))


def indexrequest(request):
	return render_to_response('indexrequest.html',RequestContext(request,locals()))

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
	return HttpResponseRedirect('/index/')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/index/')
	else:
		form = UserCreationForm()
	return render_to_response('indexregister.html',RequestContext(request,locals()))

def accounts(request):
	return render_to_response('/accounts/')

def fblog(request):
	return render_to_response('fblog.html')