from urllib import response
from django.shortcuts import render
from .models import Articulo
from .serializer import ArticuloSerializer
from rest_framework import viewsets

# Create your views here.


class ArticuloViewSet(viewsets.ModelViewSet):
    
    
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    template_name = 'articulo/index.html'
    
    def post(self,request):
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data,status=201)
        return response(serializer.errors,status=400)
    
    def deleteArticulo(self,request,pk):
        articulo = Articulo.objects.get(id=pk)
        articulo.delete()
        return response(status=204)
        
# Create your views here.
