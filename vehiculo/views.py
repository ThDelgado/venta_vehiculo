from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Vehiculo
# usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponseForbidden

#ingreso de vehiculos
from .forms import  VehiculoForm



class VehiculoView(LoginRequiredMixin, ListView):
    model = Vehiculo 
    template_name = "vehiculo/vehiculolist.html"
    context_object_name = "vehiculos"
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class UserRegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('index') #redirecciona el usuario a una vista si es valido el usuario
    
    
    def form_valid(self, form):
        user = form.save()
        

        permiso = Permission.objects.get(codename='visualizar_catalogo')
        user.user_permissions.add(permiso)
        
        messages.success(self.request,'Registro exitoso')
        return super().form_valid(form)
 
    
def add_vehiculo(request):
    if not request.user.is_staff:
        return HttpResponseForbidden('No tiene permiso para acceder a esta pagina')
    
    form = VehiculoForm() 
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        else:
            form = VehiculoForm()
            
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user =  True
    success_url = reverse_lazy('vehiculoslist') #redirecciona el usuario a una vista si es valido el usuario

    def form_valid(self, form):
        messages.success(self.request,'Login exitoso')
        return super().form_valid(form)

# por defecto se redirige a una cuenta profile/accounts si para emviar a otro lado agrega funcion: 
     
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url

class UserLogoutView(LogoutView):
    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Ha cerrado la sesion exitosamente")
        return super().dispatch(request, *args, **kwargs)

