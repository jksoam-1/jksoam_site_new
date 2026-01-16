from django.urls import path
from .views import learning_list, learning_detail

urlpatterns = [
    path("", learning_list, name="learning_list"),
    path("<slug:slug>/", learning_detail, name="learning_detail"),
]
