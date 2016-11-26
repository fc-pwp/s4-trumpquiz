
from django import forms


class StartQuizForm(forms.Form):
    username = forms.CharField(label='당신의 이름은?', min_length=2, max_length=20)

