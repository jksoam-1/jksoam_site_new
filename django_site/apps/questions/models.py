from django.db import models

class Question(models.Model):
    question = models.TextField(max_length=600)  # ~100 words safe
    answer = models.TextField(blank=True)

    asked_at = models.DateTimeField(auto_now_add=True)

    is_answered = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question[:50]
