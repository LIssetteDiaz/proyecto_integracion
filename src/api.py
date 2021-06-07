from rest_framework.response import Response
from .serializers import CategoriaSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Categoria
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

    