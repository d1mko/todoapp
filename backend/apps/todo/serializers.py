from rest_framework import serializers
from .models import Todo


class SubTodoSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class TodoSerializer(serializers.ModelSerializer):
    parent_id = serializers.ReadOnlyField(source='parent.id', required=False)
    children = SubTodoSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'content', 'color', 'children', 'parent_id']
