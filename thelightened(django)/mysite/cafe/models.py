from django.db import models
from tinymce.models import HTMLField
from django.forms import ModelForm
class MyModel(models.Model):
    	content = HTMLField()
    	def __unicode__(self):
    		return self.content

class IndexImage(models.Model):
        name = models.CharField(max_length=20)
        image = models.ImageField(upload_to = 'images')
        # def image_tag(self):
        #     return u'<img src="%s" />' % self.cover.url

        def __unicode__(self):
            return self.name

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