from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    # re_path(r'^(?P<slug>[\w-]+)/$', views.article_details),
    path('<slug>/', views.article_details, name='detail'),
]