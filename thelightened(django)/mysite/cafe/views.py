from django.shortcuts import render_to_response
from cafe.models import IndexImage, MyModel


def index(request):
	return render_to_response('index.html')

def test(request):
	return render_to_response('test.html')
	
def coffeebeans(request):
	return render_to_response('coffeebeans.html')

