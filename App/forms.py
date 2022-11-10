from django.forms import ModelForm,TextInput,EmailInput
from App.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__' #Se indica que se usan todos los atributos de nuestro modelo 
        widgets ={
            'nombre': TextInput(attrs={'class':'form-control','type':'text','pattern':'[A-Za-z]{3,25}'}),
            'apellido':TextInput(attrs={'class':'form-control','type':'text','pattern':'[A-Za-z]{3,25}'}),
            'correo':EmailInput(attrs={'class':'form-control','type':'email'})
        } 
        #Se indica los campos a nivel html, se realiza dos diccionarios. 
        #El primero dicc: contiene los nombres de los campos y como valor se indica que es una cajas de texto y de correo
        #El segundo dicc: se indica cuales son los atributos a nivel html. 
