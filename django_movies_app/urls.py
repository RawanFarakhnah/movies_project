from django.urls import path
from django_movies_app import views

urlpatterns = [
    path('', views.root, name='root'),
]