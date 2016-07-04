from django import forms
from .models import Facturacion
from .models import Cliente
from .models import Reclamos

#class FacturacionForm(forms.ModelForm):
#    class Meta:
#        model = Facturacion
#        fields = ('title', 'text',)


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'apellido','dni','mail',)

class FacturacionForm(forms.ModelForm):

    class Meta:
        model = Facturacion
        fields = (
                'empleado',
                'cliente',
                'producto',
                'cantidad_productos',
                'forma_de_pago',
                'precio_total')


class ReclamosForm(forms.ModelForm):

    class Meta:
        model = Reclamos
        fields = (
                'cliente',
                'empleado',
                'reclamo',
                'producto',
                'descripcion')
