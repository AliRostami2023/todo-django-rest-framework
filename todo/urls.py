from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.TodoListApiView.as_view()),
    path('create/', views.TodoCreateApiView.as_view()),
    path('update/<pk>/', views.TodoUpdateApiView.as_view()),
]

