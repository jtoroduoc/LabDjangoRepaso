from django.contrib import admin
from .models import Producto, Movimiento

# Register your models here.
admin.site.register(Producto)
admin.site.register(Movimiento)