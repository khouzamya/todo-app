from django.urls import path
from .api.todo_list import TodoCreateList,TodoDetailList
from .api.todo_item import TodoItemCreateList,TodoItemDetails

urlpatterns = [
    path('todos/', TodoCreateList.as_view()),
    path('todos/<int:pk>/', TodoDetailList.as_view()),
    path('todo/items/<int:list_id>/', TodoItemCreateList.as_view()),
    path('todo/items/<int:list_id>/<int:pk>/', TodoItemDetails.as_view()),
]