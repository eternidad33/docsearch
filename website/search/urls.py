from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    # path=/polls/
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('<str:keyword>', views.search, name='search'),
    path('article/<str:articleurl>', views.articleDetail, name='article'),
    path('author/<str:authorurl>', views.authorDetail, name='author'),
    path('organization/<str:organizationUrl>', views.organizationDetail, name='organization'),
    path('source/<str:sourceUrl>', views.sourceDetail, name='source'),
]
