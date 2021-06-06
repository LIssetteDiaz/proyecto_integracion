
from django.contrib import admin

from .models import Empleado,Categoria,Tipo_producto,Marca,Producto,Cliente,Artista,Venta,Detalle_venta,Pais,Region,Comuna,Sucursal


admin.site.register(Empleado)
admin.site.register(Categoria)
admin.site.register(Tipo_producto)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Artista)
admin.site.register(Venta)
admin.site.register(Detalle_venta)
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Sucursal)