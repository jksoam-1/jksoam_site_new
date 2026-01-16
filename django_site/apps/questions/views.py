from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm

def questions_page(request):
    form = QuestionForm()

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/questions/")

    questions = Question.objects.filter(
        is_approved=True,
        is_answered=True
    ).order_by("-asked_at")

    return render(
        request,
        "questions/questions.html",
        {
            "form": form,
            "questions": questions
        }
    )
