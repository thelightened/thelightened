from django.contrib import admin
from . import models

# Register your models here.

# from django.forms import ModelForm
from mce_filebrowser.admin import MCEFilebrowserAdmin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
class MyModelAdmin(MCEFilebrowserAdmin):
    pass

class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    # formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
admin.site.register(models.IndexImage)
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.MyModel, MyModelAdmin)
admin.site.register(models.User)
# admin.site.register(models.Tag)


