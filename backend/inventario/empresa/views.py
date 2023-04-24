from urllib import response
from django.shortcuts import get_object_or_404, render
from  .models import Empresa

# Create your views here.


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('id')
    serializer_class = EmpresaSerializer
    template_name = 'empresa/index.html'
    
    def get (self, request,id):
        empresa =get_object_or_404(Empresa, id=id)
        serializer = EmpresaSerializer(empresa)
        return response({'serializer':serializer,'empresa':empresa},template_name='index.html')