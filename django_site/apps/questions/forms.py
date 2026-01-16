from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question"]
        widgets = {
            "question": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Ask your question (max 100 words)..."
            })
        }

    def clean_question(self):
        data = self.cleaned_data["question"]
        if len(data.split()) > 100:
            raise forms.ValidationError("Question must be within 100 words.")
        return data
