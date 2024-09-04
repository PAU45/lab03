from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Propietario, Vehiculo, Registro
from .forms import PropietarioForm, VehiculoForm, RegistroForm
from django.contrib import messages
# Vista de inicio de sesión
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User  # Asegúrate de importar User
@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar credenciales fijas
        if username == "admin" and password == "123":
            user, created = User.objects.get_or_create(username=username)
            login(request, user)  # Iniciar sesión
            return redirect('admin_panel')  # Redirige al panel de administración
        else:
            print("Credenciales incorrectas")  # Para depurar
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})

    return render(request, 'login.html')
# Vista del panel de administración
@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')  # Asegúrate de que este archivo exista

# Propietarios
@login_required
def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'propietarios/registrar.html', {'form': form})

# Listar propietarios
@login_required
def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietarios/listar.html', {'propietarios': propietarios})

@login_required
def editar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('listar_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'propietarios/editar.html', {'form': form})

# Vehículos
@login_required
def registrar_vehiculo(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.propietario = propietario
            vehiculo.save()
            return redirect('listar_vehiculos', propietario_id=propietario.id)
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/registrar.html', {'form': form, 'propietario': propietario})

@login_required
def listar_vehiculos(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    vehiculos = Vehiculo.objects.filter(propietario=propietario)
    return render(request, 'vehiculos/listar.html', {'vehiculos': vehiculos, 'propietario': propietario})

@login_required
def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos', propietario_id=vehiculo.propietario.id)
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/editar.html', {'form': form})

# Registros
@login_required
def registrar_ingreso(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')
    else:
        form = RegistroForm()
    return render(request, 'registros/registrar.html', {'form': form})

@login_required
def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'registros/listar.html', {'registros': registros})

@login_required
def editar_registro(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'registros/editar.html', {'form': form})
@login_required
def admin_panel(request):
    # Supongamos que obtienes un propietario específico o todos
    propietarios = Propietario.objects.all()  # O filtra según lo necesites
    return render(request, 'admin_panel.html', {'propietarios': propietarios})

from django.shortcuts import redirect

def home(request):
    return redirect('login')  # Redirigir a la página de inicio de sesión



from .models import Registro

def eliminar_registro(request, id):
    registro = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar_registros')  # Asegúrate de que este nombre coincida con el definido en urls.py
    return redirect('listar_registros')  # Asegúrate de que este nombre coincida con el definido en urls.py

def eliminar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)  # Usa la variable `propietario` en lugar de `Propietario`
    if request.method == 'POST':
        propietario.delete()
        return redirect('listar_propietarios')  # Redirige a la vista de lista de propietarios
    return redirect('listar_propietarios')  # Re # Asegúrate de que este nombre coincida con el definido en urls.py


from django.shortcuts import get_object_or_404, redirect
from .models import Vehiculo

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    propietario_id = vehiculo.propietario.id  # Obtén el ID del propietario asociado
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('listar_vehiculos', propietario_id=propietario_id)  # Redirige con el ID del propietario
    return redirect('listar_vehiculos', propietario_id=propietario_id)