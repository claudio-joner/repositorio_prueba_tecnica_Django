from django.urls import path
from App import views

urlpatterns = [
    path('', views.mostrarUsuarios , name='inicio'),
    path('registrarUsuario', views.registrarUsuario )
]