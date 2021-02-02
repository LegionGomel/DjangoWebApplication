"""Define URL schemes for learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Homepage
    url(r'^$', views.index, name='index'),
    # All topics output
    url(r'^topics/$', views.topics, name='topics'),
    # Page with extended info about selected topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
