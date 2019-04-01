from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name = 'fichesVita'
urlpatterns = [
	path('', views.vitamineA, name='vitamineA'),
    path('vitamineA', views.vitamineA, name='vitamineA'),
    # path('vitamineB', views.vitamineB, name='vitamineB'),
]
