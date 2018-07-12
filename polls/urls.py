from django.urls import path
from . import views
from . import test
app_name = 'polls'
urlpatterns = [
    path('<int:question_id>/', views.index, name='index'),

    path('<int:question_id>/drawn', test.drawn, name='drawsn'),
    path('vote', views.vote, name='vote'),
    path('esc', test.rank2, name='drawn'),
    path('esr', views.rank1, name='rank'),

]