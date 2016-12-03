from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.flights, name='flights'),
    url(r'^delete/(?P<id>[\w]+)/$', views.delete_flight),
    url(r'^add', views.make_flight, name='make_flight'),
    url(r'^edit/(?P<id>[\w]+)/$', views.edit_flight, name='edit'),
    url(r'^top', views.top_companies, name='top_companies'),
]