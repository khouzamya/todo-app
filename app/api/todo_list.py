from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from app.serializer import TodoCreateListSerializer,TodoDetailListSerializer
from ..models import TodoList,TodoItem
from django.db.models import Prefetch

class TodoCreateList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = [JWTAuthentication]
	serializer_class = TodoCreateListSerializer
	filter_backends = [filters.SearchFilter,filters.OrderingFilter]
	search_fields = ['title','user__username']
	ordering_fields = ['id','title','created_at']
	ordering = ['title']
	def get_queryset(self):
		return TodoList.objects.filter(deleted_at=None).select_related('user')


class TodoDetailList(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = [JWTAuthentication]
	serializer_class = TodoDetailListSerializer
	def get_queryset(self):
		return TodoList.objects.filter(deleted_at=None).prefetch_related(Prefetch('todoitem',queryset=TodoItem.objects.filter(deleted_at=None)))

		
		
