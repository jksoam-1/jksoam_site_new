from django.contrib import admin
from .models import HomeItem

@admin.register(HomeItem)
class HomeItemAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_filter = ("is_active",)
    ordering = ("order",)
