from django import forms
from models import Post

class FacturacionForm(forms.ModelForm):

    class Meta:
        model = Facturacion
        fields = ('title', 'text',)
