from django.urls import path
from todo import views

urlpatterns = [
    path('todo/', views.todo_list, name='list-todos'),
    path('todo/<int:pk>/', views.todo_detail, name='get-todo')
]
