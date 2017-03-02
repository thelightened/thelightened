from django.db import models
from tinymce.models import HTMLField
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
class MyModel(models.Model):
    	content = HTMLField()
    	def __unicode__(self):
    		return self.content

class IndexImage(models.Model):
        name = models.CharField(max_length=20)
        image = models.ImageField(upload_to = 'images')
        def __unicode__(self):
            return self.name
        # def image_tag(self):
        #     return u'<img src="%s" />' % self.cover.url
@receiver(pre_delete, sender=IndexImage)

def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

        

# class Tag(models.Model):
#     slug = models.SlugField(max_length=200, unique=True)

#     def __unicode__(self):
#         return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()
    coverr = models.ImageField(upload_to = 'images')
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

