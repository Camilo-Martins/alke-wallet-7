from django import forms
from .models import Usuario, Cuenta, Transaccion


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo']


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['usuario', 'numero_cuenta', 'saldo']


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['cuenta', 'tipo', 'monto', 'descripcion']