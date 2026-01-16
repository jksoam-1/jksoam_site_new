from django.urls import path
from .views import devops

urlpatterns = [
    path("", devops, name="devops"),
]
