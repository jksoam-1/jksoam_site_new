from django.shortcuts import render
from .models import HomeItem

def home(request):
    items = HomeItem.objects.filter(is_active=True)
    return render(request, "home/home.html", {"items": items})
