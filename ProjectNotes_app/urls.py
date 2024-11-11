from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project_list, name='project_list'),  
    path('project/<str:slug>', views.project_detail, name='project_detail'),  
    path('notes/', views.notes_list, name='notes_list'), 
]

