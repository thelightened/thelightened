# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

def login(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/indexhomepage/')

	username = request.POST.get('username','')
	password = request.POST.get('password','')

	user = auth.authenticate(username=username,password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/indexhomepage/')
	else:
		return render_to_response('login.html',RequestContext(request,locals()))

def indexhomepage(request):	
	return render_to_response('indexhomepage.html',RequestContext(request,locals()))

def logout(request):	
	auth.logout(request)
	return HttpResponseRedirect('/indexhomepage/')
