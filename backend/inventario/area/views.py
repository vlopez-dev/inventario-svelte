from urllib import response
from django.shortcuts import render
from .models import Area
from .serializers import AreaSerializer
from rest_framework import viewsets

# Create your views here.


class AreaViewSet(viewsets.ModelViewSet):
    
    
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    template_name = 'area/index.html'
    
    def post(self,request):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data,status=201)
        return response(serializer.errors,status=400)
    
    def deleteArea(self,request,pk):
        area = Area.objects.get(id=pk)
        area.delete()
        return response(status=204)
        