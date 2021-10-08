from django import urls
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('postcreate/', views.PostCreate.as_view(), name='postcreate'),
]