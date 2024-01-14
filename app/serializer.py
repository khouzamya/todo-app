from rest_framework import serializers
from .models import TodoList,TodoItem
from datetime import datetime
class TodoItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoItem
		fields = ('id','list','description','completed_at','created_at','updated_at')
	def to_internal_value(self, data):
		data["list"] = self.context.get('request').parser_context.get('kwargs').get('list_id')
		data["created_at"] = datetime.now()
		data["updated_at"] = datetime.now()
		return super().to_internal_value(data)
	def validate(self, attrs):
		list_id = self.context.get('request').parser_context.get('kwargs').get('list_id')
		try:
			TodoList.objects.get(id=list_id,deleted_at=None)
		except:
			raise serializers.ValidationError(
               {'detail': 'Not found.'},
                code=404,
            )
		return super().validate(attrs)
	
class TodoItemDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoItem
		fields = ('id','description','completed_at','updated_at')
	def to_internal_value(self, data):
		if data.get("completed") and not self.instance.completed_at:
			data["completed_at"] = datetime.now()
		data["updated_at"] = datetime.now()
		return super().to_internal_value(data)
	def validate(self, attrs):
		print("here")
		list_id = self.context.get('request').parser_context.get('kwargs').get('list_id')
		try:
			check_todo = TodoList.objects.get(id=list_id,deleted_at=None)
		except:
			raise serializers.ValidationError(
               {'detail': 'Not found.'},
                code=404,
            )
		if check_todo.user != self.context.get('request').user:
			raise serializers.ValidationError(
               {'detail': 'Not found.'},
                code=404,
            )			
		return super().validate(attrs)


class TodoCreateListSerializer(serializers.ModelSerializer):
	user_info = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = TodoList
		fields = ('id','user_info','user','title','completed_at','created_at','updated_at')
		extra_kwargs = {
			'user': {'write_only': True},
		}
	def to_internal_value(self, data):
		data["user"] = self.context["request"].user.id
		data["created_at"] = datetime.now()
		data["updated_at"] = datetime.now()
		return super().to_internal_value(data)
	def get_user_info(self,obj):
		return {'fname': obj.user.first_name,'lname':obj.user.last_name,'username':obj.user.username,'id':obj.user.id}
	
class TodoDetailListSerializer(serializers.ModelSerializer):
	todoitem = TodoItemSerializer(many=True, read_only=True)
	class Meta:
		model = TodoList
		fields = ('id','title','completed_at','updated_at','todoitem')
	def to_internal_value(self, data):
		if data.get("completed") and not self.instance.completed_at:
			data["completed_at"] = datetime.now()
		data["updated_at"] = datetime.now()
		return super().to_internal_value(data)
	
	def validate(self, attrs):
		if self.instance.user != self.context.get('request').user:
			raise serializers.ValidationError(
               {'detail': 'Not found.'},
                code=404,
            )
		return super().validate(attrs)





