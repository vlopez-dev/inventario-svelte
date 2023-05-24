from django.conf import settings
from django.urls import path,include
from rest_framework import routers
from django.conf.urls.static import static

from . import views



router = routers.DefaultRouter()
router.register(r'articulo', views.ArticuloViewSet)
router.register(r'tipo', views.TipoViewSet)



urlpatterns = [
    path('', include(router.urls)),
    # path('tipos/', views.TipoViewSet, name='tipos-list'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
