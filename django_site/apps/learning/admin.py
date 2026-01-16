from django.contrib import admin
from .models import Learning

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    list_filter = ("published",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
