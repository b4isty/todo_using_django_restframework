from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDoElements
from .serializers import ToDoSerializer
from rest_framework import status
class ToDoView(APIView):
    def get(self,request):
        todo = ToDoElements.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












# class ToDoViewSet(viewsets.ModelViewSet):
#     queryset = ToDoElements.objects.all()
#     serializer_class = ToDoSerializer

