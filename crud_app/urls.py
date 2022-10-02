from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),

    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('complete_task/<int:pk>', views.complete_task, name='complete_task'),


]
