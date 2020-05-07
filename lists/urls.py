from django.conf.urls import url
from django.urls import path

from lists import views


urlpatterns = [
    path('new', views.new_list, name='new_list'),
    url(r'(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item')
]