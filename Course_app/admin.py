from django.contrib import admin
from Course_app.models import Card_list, Topic, TopicDetail, MCQ, FillInTheBlank
from django.db import models  # Add this import to use models.TextField
from tinymce.widgets import TinyMCE  # Import TinyMCE widget

# Admin configuration for TinyMCE
class TopicDetailAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 100, 'rows': 50})},
    }

class CardListAdmin(admin.ModelAdmin):
    pass

class TopicAdmin(admin.ModelAdmin):
    pass
class MCQAdmin(admin.ModelAdmin):
    pass
class FillInTheBlankAdmin(admin.ModelAdmin):
    pass

# Register models with admin
admin.site.register(Card_list, CardListAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicDetail, TopicDetailAdmin)

admin.site.register(MCQ,MCQAdmin)
admin.site.register(FillInTheBlank,FillInTheBlankAdmin)