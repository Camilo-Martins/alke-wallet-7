from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('cuentas/', views.lista_cuentas, name='lista_cuentas'),
    path('cuentas/crear/', views.crear_cuenta, name='crear_cuenta'),
    path('cuentas/editar/<int:pk>/', views.editar_cuenta, name='editar_cuenta'),
    path('cuentas/eliminar/<int:pk>/', views.eliminar_cuenta, name='eliminar_cuenta'),

    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('transacciones/crear/', views.crear_transaccion, name='crear_transaccion'),
    path('transacciones/editar/<int:pk>/', views.editar_transaccion, name='editar_transaccion'),
    path('transacciones/eliminar/<int:pk>/', views.eliminar_transaccion, name='eliminar_transaccion'),
]