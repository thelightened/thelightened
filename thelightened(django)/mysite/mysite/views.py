# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from cafe.views import index
def here(request):
	return HttpResponse('FUCK')



