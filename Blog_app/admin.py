from django.contrib import admin
from Blog_app.models import BlogPost
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 100, 'rows': 50})},
    }



admin.site.register(BlogPost,BlogPostAdmin)