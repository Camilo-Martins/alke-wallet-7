from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Cuenta, Transaccion
from .forms import UsuarioForm, CuentaForm, TransaccionForm


def inicio(request):
    return render(request, 'wallet/inicio.html')


# -------------------
# USUARIOS
# -------------------

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'wallet/usuarios/lista.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'wallet/usuarios/form.html', {'form': form, 'titulo': 'Crear usuario'})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'wallet/usuarios/form.html', {'form': form, 'titulo': 'Editar usuario'})


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'wallet/usuarios/eliminar.html', {'objeto': usuario, 'tipo': 'usuario'})


# -------------------
# CUENTAS
# -------------------

def lista_cuentas(request):
    cuentas = Cuenta.objects.select_related('usuario').all()
    return render(request, 'wallet/cuentas/lista.html', {'cuentas': cuentas})


def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm()
    return render(request, 'wallet/cuentas/form.html', {'form': form, 'titulo': 'Crear cuenta'})


def editar_cuenta(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    if request.method == 'POST':
        form = CuentaForm(request.POST, instance=cuenta)
        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm(instance=cuenta)
    return render(request, 'wallet/cuentas/form.html', {'form': form, 'titulo': 'Editar cuenta'})


def eliminar_cuenta(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    if request.method == 'POST':
        cuenta.delete()
        return redirect('lista_cuentas')
    return render(request, 'wallet/cuentas/eliminar.html', {'objeto': cuenta, 'tipo': 'cuenta'})


# -------------------
# TRANSACCIONES
# -------------------

def lista_transacciones(request):
    transacciones = Transaccion.objects.select_related('cuenta', 'cuenta__usuario').all()
    return render(request, 'wallet/transacciones/lista.html', {'transacciones': transacciones})


def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()
    return render(request, 'wallet/transacciones/form.html', {'form': form, 'titulo': 'Crear transacción'})


def editar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm(instance=transaccion)
    return render(request, 'wallet/transacciones/form.html', {'form': form, 'titulo': 'Editar transacción'})


def eliminar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if request.method == 'POST':
        transaccion.delete()
        return redirect('lista_transacciones')
    return render(request, 'wallet/transacciones/eliminar.html', {'objeto': transaccion, 'tipo': 'transacción'})