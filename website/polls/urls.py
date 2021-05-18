from django.urls import path

from . import views

# 命名空间
app_name = 'polls'

# 配置APP路由


urlpatterns = [
    # path=/polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path=/polls/5
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path=/polls/5/results
    # path('<int:question_id>/results', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path=/polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),

]
