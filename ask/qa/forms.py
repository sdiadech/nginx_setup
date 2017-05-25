from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer
from django.contrib.auth import authenticate


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text',)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', 'question',)