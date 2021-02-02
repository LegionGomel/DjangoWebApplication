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
    # Page for add a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for add a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
