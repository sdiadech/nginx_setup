from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, question_pk):
    q = get_object_or_404(Question, pk=question_pk)
    answers = Answer.objects.filter(question=q)

    return render(request, 'question.html', {'question': q, 'answers': answers})


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