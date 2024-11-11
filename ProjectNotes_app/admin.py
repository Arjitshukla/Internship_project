from django.contrib import admin
from ProjectNotes_app.models import Notes_Section,Project_Section
# Register your models here.

admin.site.register((Notes_Section))
admin.site.register((Project_Section))