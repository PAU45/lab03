from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('propietarios/registrar/', views.registrar_propietario, name='registrar_propietario'),
    path('propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('propietarios/editar/<int:propietario_id>/', views.editar_propietario, name='editar_propietario'),

    path('vehiculos/registrar/<int:propietario_id>/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('vehiculos/<int:propietario_id>/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculos/editar/<int:vehiculo_id>/', views.editar_vehiculo, name='editar_vehiculo'),

    path('registros/registrar/', views.registrar_ingreso, name='registrar_ingreso'),
    path('registros/', views.listar_registros, name='listar_registros'),
    path('registros/editar/<int:registro_id>/', views.editar_registro, name='editar_registro'),

    path('admin/', views.admin_panel, name='admin_panel'),
    path('login/', views.login_view, name='login'),
       path('eliminar_registro/<int:id>/', views.eliminar_registro, name='eliminar_registro'),
        path('eliminar_propietario/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),
        path('eliminar_vehiculo/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]