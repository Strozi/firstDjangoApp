from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'), # $ means end of string -> other part of url is defined in global urls.py
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name ='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url('^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]