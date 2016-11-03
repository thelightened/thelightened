from django.contrib import admin
from cafe.models import IndexImage, MyModel
from mce_filebrowser.admin import MCEFilebrowserAdmin
class MyModelAdmin(MCEFilebrowserAdmin):
    pass
admin.site.register(IndexImage)
admin.site.register(MyModel, MyModelAdmin)
