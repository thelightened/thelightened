from django.shortcuts import render_to_response
from cafe.models import IndexImage, MyModel


def index(request):
	return render_to_response('index.html')

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

