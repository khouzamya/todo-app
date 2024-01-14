from rest_framework import filters
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from app.serializer import TodoItemSerializer,TodoItemDetailsSerializer
from ..models import TodoItem


class TodoItemCreateList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = [JWTAuthentication]
	serializer_class = TodoItemSerializer
	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['id']
	ordering = ['id']
	def get_queryset(self):
		return TodoItem.objects.filter(list__user=self.request.user,list__deleted_at=None,list__id=self.kwargs.get('list_id'),deleted_at=None)

class TodoItemDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = [JWTAuthentication]
	serializer_class = TodoItemDetailsSerializer
	def get_queryset(self):
		return TodoItem.objects.filter(list__deleted_at=None,deleted_at=None)
		
		