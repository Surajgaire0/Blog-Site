from django.contrib import admin
from .models import Posts
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostsAdmin(SummernoteModelAdmin,ImportExportModelAdmin):
    models=Posts
    list_display=('title','publication_date','author')
    summernote_fields = ('description',)

admin.site.register(Posts, PostsAdmin)