from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import Question, Answer
from .forms import AskForm, AnswerForm

import string
import random

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, question_pk):
    q = get_object_or_404(Question, pk=question_pk)
    answers = Answer.objects.filter(question=q)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = q
            answer.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = AnswerForm(initial={'question': q})

    return render(request, 'question.html', {'question': q, 'answers': answers})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            try:
                question.author = request.user
            except ValueError:
                question.author = random_user()
            question.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_pk': question.pk}))
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def random_user():
    name = ''
    while True:
        for i in range(10):
            name += random.choice(string.ascii_letters)
        try:
            User.objects.get(username=name)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=name, email='hi@there.com', password='666')
            break
    return user


def popular(request):
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular/?page='
    page_num = request.GET.get('page')
    try:
        questions = paginator.page(page_num)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'popular.html', {'questions': questions, 'paginator': paginator})


def new(request):
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page_num = request.GET.get('page')
    try:
        questions = paginator.page(page_num)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': questions, 'paginator': paginator})