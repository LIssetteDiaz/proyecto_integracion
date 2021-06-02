from django.db import models

# Create your models here.

##Base de datos Distribuuidora

##Empleados
class Empleado(models.Model):
    rut_id = models.AutoField(primary_key=True)  
    sueldo = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.rut

##Grupos musicales
class GruposMusicales(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

##Instrumentos 
class Instrumentos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

##Accesorios
class Accesorios(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


##Fabricantes 
class fabricantes(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

##Marcas
class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

##Compra
class Compra(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


##Clientes
class Cliente(models.Model):
    rut = models.IntegerField(null=False)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    papellido = models.CharField(max_length=20)
    sapellido = models.CharField(max_length=20)
    contacto = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    

    def __str__(self):
        return self.rut

##Artistas
class Artistas(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

##Distribuidoras tiendas
class tiendas(models.Model):
    cod_tiendas = models.ForeignKey(Persona,on_delete=models.CASCADE,default=0)
    cod_sucursal = models.CharField(max_length=10)
    direccion = models.TextField(default=0)
    
    def __str__(self):
        return self.direccion


##Venta
class Venta(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



##Region
class Region(models.Model):
    nombre = models.CharField(max_length= 30)

    def __str__(self):
        return self.nombre


##Comuna
class Comuna(models.Model):
    cod_region= models.CharField(max_length=40)
    nombre = models.TextField(max_length= 30)

    def __str__(self):
        return self.nombre


##Ducursal
class Sucursal(models.Model):
    cod_comuna = models.ForeignKey(Persona,on_delete=models.CASCADE,default=0)
    cod_sucursal = models.CharField(max_length=10)
    direccion = models.TextField(default=0)
    
    def __str__(self):
        return self.direccion


##Pais
class Comuna(models.Model):
    cod_Comuna = models.ForeignKey(Persona,on_delete=models.CASCADE,default=0)
    cod_sucursal = models.CharField(max_length=10)
    direccion = models.TextField(default=0)
    
    def __str__(self):
        return self.direccion


##Trabajador
class Trabajador(models.Model):
    rut = models.IntegerField(null=False)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    papellido = models.CharField(max_length=20)
    sapellido = models.CharField(max_length=20)
    contacto = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    

    def __str__(self):
        return self.rut
