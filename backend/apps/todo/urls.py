from django.urls import path

from . import views


urlpatterns = [
    path("", views.TodoListCreate.as_view(), name="todo-list-create"),
    path("<int:pk>/", views.TodoDetail.as_view(), name="todo-detail"),
    path("<int:parent_id>/replies/", views.TodoListCreate.as_view()),
]