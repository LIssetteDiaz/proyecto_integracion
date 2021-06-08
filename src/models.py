from django.db import models
##Base de datos Distribuidora

##Empleado
class Empleado(models.Model):
    rut = models.IntegerField(null=False)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    contacto = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "empleado"
    
    def __str__(self):
        return self.rut

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "categoria"

    def __str__(self):
        return self.descripcion

class Tipo_producto(models.Model):
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "tipo_producto"

    def __str__(self):
        return self.descripcion

##Marca
class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "marca"

    def __str__(self):
        return self.nombre

##Instrumentos 
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(null=False)
    imagen = models.ImageField(default=None,upload_to="instrumentos", blank=True, null=True)
    tipo_producto = models.ForeignKey(Tipo_producto,on_delete=models.CASCADE,default=0)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "producto"

    def __str__(self):
        return self.nombre

##Clientes
class Cliente(models.Model):
    rut = models.IntegerField(null=False)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "cliente"
    
    def __str__(self):
        return self.rut

##Artistas
class Artista(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "artista"

    def __str__(self):
        return self.nombre

##Venta(VER)
class Venta(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,default=0)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "venta"

    def __str__(self):
        return self.nombre

class Detalle_venta(models.Model):
    cantidad = models.CharField(max_length=30)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,default=0)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "detalle_venta"

    def __str__(self):
        return self.nombre

##Pais
class Pais(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = "pais"
    
    def __str__(self):
        return self.direccion

##Region
class Region(models.Model):
    nombre = models.CharField(max_length= 30)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "region"

    def __str__(self):
        return self.nombre

##Comuna
class Comuna(models.Model):
    nombre = models.TextField(max_length= 30)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "comuna"

    def __str__(self):
        return self.nombre

##Sucursal
class Sucursal(models.Model):
    direccion = models.TextField(default=0)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,default=0)

    class Meta:
        verbose_name = "sucursal"

    def __str__(self):
        return self.direccion


