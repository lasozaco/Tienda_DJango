from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} <{self.correo}>"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ("CREADO", "Creado"),
        ("PAGADO", "Pagado"),
        ("ENVIADO", "Enviado"),
        ("CERRADO", "Cerrado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    estado = models.CharField(max_length=10, choices=ESTADOS, default="CREADO")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.pk} - {self.cliente.nombre} ({self.estado})"
    
class PedidoItem(models.Model):
        pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="items")
        producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="items")
        cantidad = models.PositiveBigIntegerField(default=1)
        precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

        class Meta:
            '''
            No se permitirá que exitan dos filas con la misma combinación de pedido y producto.
            '''
            unique_together= ("pedido", "producto")

