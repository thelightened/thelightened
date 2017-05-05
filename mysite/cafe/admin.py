from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from . import models
from .models import User

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

# class ProfileInline(admin.StackedInline):
#     model = User
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
#     list_select_related = ('profile', )

#     def get_location(self, instance):
#         return instance.profile.location
#     get_location.short_description = 'Location'

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)