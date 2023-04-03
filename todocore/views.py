from django.http import JsonResponse
from datetime import datetime
from rest_framework.views import APIView
from todocore.models import Task
from todocore.serializer import TaskSerializer
from rest_framework.response import Response


class TaskListView(APIView):
    serializer_class=TaskSerializer

    def get(self,request):
        tasks=Task.objects.all()
        task_serializer=self.serializer_class(tasks,many=True)
        return Response(
            {"tasks":task_serializer.data}
        )
    def post(self,request):
        task_data=request.data
        task_serializer=self.serializer_class(data=task_data)
        if task_serializer.is_valid(raise_exception=True):
            task_serializer.save()
        return Response(task_serializer.data)


class TaskUpdateView(APIView):
    serializer_class=TaskSerializer

    def put(self,request,id):
        task_data = request.data
        existing_task = Task.objects.get(id=id)
        task_serializer = self.serializer_class(existing_task, data=task_data)
        if task_serializer.is_valid(raise_exception=True):
            task_serializer.save()
        return Response(
            task_serializer.data
        )

    def delete(self, request, id):
        delete_task = Task.objects.get(id=id)
        delete_task.delete()
        task_serializer = self.serializer_class(delete_task)
        return JsonResponse(
            task_serializer.data
        )



