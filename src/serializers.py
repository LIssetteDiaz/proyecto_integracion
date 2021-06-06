from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Empleado, GruposMusicales


''' class PersonaSerializer(serializers.Serializer):
    rut = serializers.IntegerField(read_only=True)
    dv = serializers.CharField()
    nombre = serializers.CharField()
    papellido = serializers.CharField()
    sapellido = serializers.CharField()
    contacto = serializers.CharField()
    email = serializers.EmailField()
    
    
    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Persona.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.rut = validated_data.get('rut', instance.rut)
        instance.dv = validated_data.get('name', instance.name)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.papellido = validated_data.get('papellido', instance.papellido)
        instance.sapellido = validated_data.get('sapellido', instance.sapellido)
        instance.validated_data.get('contacto', instance.contacto)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

 '''







class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('rut_id', 'sueldo')
        


class PostresSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruposMusicales
        fields = ('nombre', 'descripcion')