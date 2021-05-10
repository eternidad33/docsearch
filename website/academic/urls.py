from django.urls import path

from . import views
import automat

urlpatterns = [
    path('', views.index, name='index'),
]