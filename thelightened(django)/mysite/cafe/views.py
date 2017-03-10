from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from . import models
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import patterns, url
from django.views import generic

from django.core.urlresolvers import reverse_lazy 
from django.views.generic.edit import FormView 
from django.contrib.auth import authenticate, login 
from forms import RegisterForm 

from django.contrib import messages
from django.template.loader import get_template


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog.html"
    paginate_by = 6


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')


def form_valid(self, form):
    form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)
    login(self.request, user)
    return super(RegisterView, self).form_valid(form)

    
    # def logout(request):
    #     auth.logout(request)
    #     messages.add_message(request, messages.INFO, "")
    #     return redirect('/')

# def index(request):

# 	index = models.IndexImage.objects.all()
# 	return render_to_response('index.html',RequestContext(request,locals()))

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
	return render_to_response('coffeebeans.html')

def blog(request):
	return render_to_response('blog.html')

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
	return render_to_response('partnershop.html')

def cart(request):
     # if not request.user.is_authenticated():
     #    return HttpResponseRedirect('/accounts/login/?next={0}'.format(request.path))
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

def menu(request):
    return render_to_response('menu.html')

def article(request):
    return render_to_response('article.html')    

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







