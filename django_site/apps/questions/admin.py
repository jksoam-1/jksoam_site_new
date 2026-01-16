from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("short_question", "is_answered", "is_approved", "asked_at")
    list_filter = ("is_answered", "is_approved")
    search_fields = ("question",)

    def short_question(self, obj):
        return obj.question[:60]
