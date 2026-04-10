from django import forms
from .models import Producto
from .models import Cliente

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
        precio = self.cleanedd_data.get("precio")
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
