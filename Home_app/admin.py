from django.contrib import admin
from Home_app.models import ContactMessage,About_Section
# Register your models here.

admin.site.register((ContactMessage))
admin.site.register((About_Section))