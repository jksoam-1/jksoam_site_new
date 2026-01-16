from django.shortcuts import render, get_object_or_404
from .models import Learning

def learning_list(request):
    topics = Learning.objects.filter(published=True)
    return render(
        request,
        "learning/learning_list.html",
        {"topics": topics}
    )

def learning_detail(request, slug):
    topic = get_object_or_404(
        Learning,
        slug=slug,
        published=True
    )
    return render(
        request,
        "learning/learning_detail.html",
        {"topic": topic}
    )
