from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#@admin.site.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    models=Profile
    list_display=('slug','user','website')

admin.site.register(Profile,ProfileAdmin)