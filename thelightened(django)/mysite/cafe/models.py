from django.db import models
from tinymce.models import HTMLField

class MyModel(models.Model):
    	content = HTMLField()
    	def __unicode__(self):
    		return self.content

class IndexImage(models.Model):
		name = models.CharField(max_length=20)
		image = models.ImageField(upload_to = "images" )
		def __unicode__(self):
			return self.name