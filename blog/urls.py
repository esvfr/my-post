"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from . import views

app_name='blog'
urlpatterns = [
    url(r'^$', views.EKnowledgeIndex.as_view(), name='index'),
    url(r'^(?P<section>[\w]+)/$', views.ESectionView.as_view(), name='section'),
    url(r'^(?P<section>[\w]+)/(?P<article_id>[0-9]+)/$', views.EArticleView.as_view(), name='article'),
    url(r'^stat/(?P<article_id>[0-9]+)/$', views.EArticleView.as_view(), name='article_stat'),
]
