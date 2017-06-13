"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from qa import views

urlpatterns = [
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<question_pk>[0-9]+)/$', views.question, name='question'),
    url(r'^ask/', views.ask),
    url(r'^popular/', views.popular),
    url(r'^$', views.new),
]