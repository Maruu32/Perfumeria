from django import forms
from .models import Facturacion
from .models import Cliente

#class FacturacionForm(forms.ModelForm):
#    class Meta:
#        model = Facturacion
#        fields = ('title', 'text',)


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'apellido','dni','mail',)