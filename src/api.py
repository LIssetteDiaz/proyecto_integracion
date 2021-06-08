from rest_framework.response import Response
from .serializers import CategoriaSerializer, EmpleadoSerializer, MarcaSerializer, ProductoSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Categoria, Empleado, Tipo_producto, Marca, Producto
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def categoria_api_view(request):

    if request.method == 'GET':
        serializer = Categoria.objects.all()
        serializer = CategoriaSerializer(serializer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def categoria_detail_api_view(request, pk=None):

    if request.method == 'GET':
        serializer = Categoria.objects.filter(id = pk).first()
        serializer = CategoriaSerializer(serializer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Categoria.objects.filter(id = pk).first()
        serializer = CategoriaSerializer(serializer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        serializer = Categoria.objects.filter(id = pk).first()
        serializer.delete()
        return Response('Categoria eliminada')

@api_view(['GET'])
def categoria_api_view_orderBy(request, value = None):

    if request.method == 'GET':
        serializer = Categoria.objects.order_by(value)
        serializer = CategoriaSerializer(serializer, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def categoria_api_view_contains(request, text = None):

    if request.method == 'GET':
        serializer = Categoria.objects.filter(descripcion__contains=text)
        serializer = CategoriaSerializer(serializer, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def categoria_api_view_filterForId(request, id = None):

    if request.method == 'GET':
        serializer = Categoria.objects.filter(id = id)
        serializer = CategoriaSerializer(serializer, many=True)
        return Response(serializer.data)


##*********************Empleados***********************++
@api_view(['GET','POST'])
def empleado_api_view(request):

    if request.method == 'GET':
        serializer = Empleado.objects.all()
        serializer = EmpleadoSerializer(serializer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmpleadoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def empleado_detail_api_view(request, pk=None):

    if request.method == 'GET':
        serializer = Empleado.objects.filter(id = pk).first()
        serializer = EmpleadoSerializer(serializer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Empleado.objects.filter(id = pk).first()
        serializer = EmpleadoSerializer(serializer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        serializer = Empleado.objects.filter(id = pk).first()
        serializer.delete()
        return Response('Empleado eliminado')

@api_view(['GET'])
def empleado_detail_api_view_filterForName(request, name=None):

    if request.method == 'GET':
        serializer = Empleado.objects.filter(nombre = name)
        serializer = EmpleadoSerializer(serializer)
        return Response(serializer.data)

@api_view(['GET'])
def empleado_detail_api_view_filterForEmail(request, email=None):

    if request.method == 'GET':
        serializer = Empleado.objects.filter(email = email)
        serializer = EmpleadoSerializer(serializer)
        return Response(serializer.data)

##*********************Tipos producto***********************++
@api_view(['GET','POST'])
def tipoProd_api_view(request):

    if request.method == 'GET':
        serializer = Tipo_producto.objects.all()
        serializer = TipoProductoSerializer(serializer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TipoProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def tipoProd_detail_api_view(request, pk=None):

    if request.method == 'GET':
        serializer = Tipo_producto.objects.filter(id = pk).first()
        serializer = TipoProductoSerializer(serializer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Tipo_producto.objects.filter(id = pk).first()
        serializer = TipoProductoSerializer(serializer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        serializer = Tipo_producto.objects.filter(id = pk).first()
        serializer.delete()
        return Response('Tipo producto eliminado')



##*********************Marcas***********************++
@api_view(['GET','POST'])
def marca_api_view(request):

    if request.method == 'GET':
        serializer = Marca.objects.all()
        serializer = MarcaSerializer(serializer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MarcaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def marca_detail_api_view(request, pk=None):

    if request.method == 'GET':
        serializer = Marca.objects.filter(id = pk).first()
        serializer = MarcaSerializer(serializer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Marca.objects.filter(id = pk).first()
        serializer = MarcaSerializer(serializer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        serializer = Marca.objects.filter(id = pk).first()
        serializer.delete()
        return Response('Marca eliminado')



##*********************Marcas***********************++
@api_view(['GET','POST'])
def producto_api_view(request):

    if request.method == 'GET':
        serializer = Producto.objects.all()
        serializer = ProductoSerializer(serializer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def producto_detail_api_view(request, pk=None):

    if request.method == 'GET':
        serializer = Producto.objects.filter(id = pk).first()
        serializer = ProductoSerializer(serializer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Producto.objects.filter(id = pk).first()
        serializer = ProductoSerializer(serializer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        serializer = Producto.objects.filter(id = pk).first()
        serializer.delete()
        return Response('Producto eliminado')

@api_view(['GET'])
def producto_detail_api_view_filterForPrice(request, price=None):

    if request.method == 'GET':
        serializer = Producto.objects.filter(precio = price)
        serializer = ProductoSerializer(serializer)
        return Response(serializer.data)


@api_view(['GET'])
def producto_detail_api_view_filterForName(request, name=None):

    if request.method == 'GET':
        serializer = Producto.objects.filter(nombre = name)
        serializer = ProductoSerializer(serializer)
        return Response(serializer.data)
         
        