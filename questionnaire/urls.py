from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name = 'questionnaire'
urlpatterns = [
    path('', views.choixObjectif, name='choixObjectif'),
    path('choixObjectif', views.choixObjectif, name='choixObjectif'),
    
    path('addObjective/<slug:objectif_id>', views.addObjective, name='addObjective'),
    path('deleteObjective/<slug:objectif_id>', views.deleteObjective, name='deleteObjective')
]