from django.urls import path
from . import views

app_name = 'custom_news_admin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),
]
