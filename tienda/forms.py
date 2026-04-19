from django import forms
from django.forms import inlineformset_factory
from .models import Producto
from .models import Cliente, Pedido, PedidoItem



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre del producto"
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Descripción breve"
            }),
            "precio": forms.NumberInput (attrs={
                "step": "0.01",
                "min": "0"
            }),
        }

    def clean_precio(self):
        # Si el precio es negativo o cero, se lanza una excepción.
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "correo", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre completo"}),
            "correo": forms.EmailInput(attrs={"placeholder": "ejemplo@correo.com"}),
        
        }

class PedidoSimpleForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "estado"]

class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ["producto", "cantidad", "precio_unitario"]
        widgets = {
            "cantidad": forms.NumberInput(attrs={"min": "1", "step": "1"}),
            "precio_unitarios": forms.NumberInput(attrs={"min": "0", "step": "0.01"}),
        }

PedidoItemFormSet = inlineformset_factory(
    parent_model=Pedido,
    model=PedidoItem,
    form=PedidoItemForm,
    extra=1,              #cuantas filas "vacias" mostrar por defecto
    can_delete=True #permitir borrar filas

)