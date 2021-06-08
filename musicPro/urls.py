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
from src.api import categoria_api_view, categoria_detail_api_view, categoria_api_view_orderBy, categoria_api_view_contains, categoria_api_view_filterForId
from src.api import empleado_api_view, empleado_detail_api_view, empleado_detail_api_view_filterForName, empleado_detail_api_view_filterForEmail
from src.api import tipoProd_api_view, tipoProd_detail_api_view
from src.api import marca_api_view, marca_detail_api_view
from src.api import producto_api_view, producto_detail_api_view
from src.api import producto_detail_api_view_filterForPrice, producto_detail_api_view_filterForName


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='Inicio'),
    path('instrumentos/', views.GaleriaInstrumentos, name='instrumentos'),
    path('tienda/', views.carrito, name='carrito'),
    

    ##**********************Categorias
    path('api/categorias/', categoria_api_view, name='categories'),
    path('api/categorias_detail/<int:pk>', categoria_detail_api_view, name='categoriesDetail'),
    path('api/categoria_orderBy/<str:value>', categoria_api_view_orderBy, name='categoriesOrderBy'),
    path('api/categoria_contains/<str:text>', categoria_api_view_contains, name='categoriesContains'),
    path('api/categoria_filterForId/<int:id>', categoria_api_view_filterForId, name='categoriesFilter'),


    ##*************************Empleados
    path('api/empleados/', empleado_api_view, name='empleados'),
    path('api/empleados_detail/<int:pk>', empleado_detail_api_view, name='empleadosDetail'),
    path('api/empleado_filterForName/<str:name>', empleado_detail_api_view_filterForName, name='empleadosFilterName'),
    path('api/empleado_filterForEmail/<str:email>', empleado_detail_api_view_filterForEmail, name='empleadosFilterEmail'),
    
    
    ##*************************Tipos de producto
    path('api/tipos_producto/', tipoProd_api_view, name='tiposProducto'),
    path('api/tiposProd_detail/<int:pk>', tipoProd_detail_api_view, name='tiposProdDetail'),
    

    ##*************************Marcas
    path('api/marcas/', marca_api_view, name='marcas'),
    path('api/marcas_detail/<int:pk>', marca_detail_api_view, name='marcasDetail'),
    

    ##*************************Productos
    path('api/productos/', producto_api_view, name='productos'),
    path('api/productos_detail/<int:pk>', producto_detail_api_view, name='productosDetail'),
    path('api/producto_filterForName/<str:name>', producto_detail_api_view_filterForName, name='categoriesContains'),
    path('api/producto_filterForPrice/<int:price>', producto_detail_api_view_filterForPrice, name='categoriesFilter'),
    
]