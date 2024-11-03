
from django.urls import path
from . import views

urlpatterns = [
    path('vehiculo/', views.VehiculoView.as_view(), name= 'vehiculoslist'),   
    path('add/', views.add_vehiculo, name= 'add_vehiculo'),
    path('registro/', views.UserRegistroView.as_view(), name = "registro"),
    path('login/', views.UserLoginView.as_view(), name ='login'),
    path('logout/', views.UserLogoutView.as_view(), name ='logout'),

]