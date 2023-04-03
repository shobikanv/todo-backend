from rest_framework import serializers

from todocore.models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Task
        fields = "__all__"