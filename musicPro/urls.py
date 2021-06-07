"""musicPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from src import views
from django.urls import path, include
from django.contrib.auth.models import User
from src.models import Categoria
from rest_framework import routers, serializers, viewsets
from src.api import categoria_api_view, categoria_detail_api_view



# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# # Serializers define the API representation.
# class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Categoria
#         fields = ['id', 'descripcion']

# # ViewSets define the view behavior.
# class CategoriaViewSet(viewsets.ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()


# router.register(r'users', UserViewSet)
# router.register(r'categorias', CategoriaViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='Inicio'),
    path('instrumentos/', views.GaleriaInstrumentos, name='instrumentos'),
    path('tienda/', views.carrito, name='carrito'),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/categorias/', categoria_api_view, name='categories'),
    path('api/categorias_detail/<int:pk>', categoria_detail_api_view, name='categoriesDetail'),
    # path('api/crear_categoria/<int:pk>', CategoriaApi.as_view(), name='api_create_categories'),

]