from django import forms
from app.models import *
from django.contrib.auth.models import User

class EspecialidadForm(forms.ModelForm):
    
    class Meta:
        model = Especializacion
        fields = ("especialidad",)
        labels = {
            'especialidad' : 'Especialidad',
        }
        widgets = {
            'especialidad' : forms.TextInput(attrs={'class':'form-control'}),
        }
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = cliente
        fields = ("cedula",
            'nombres',
            'apellidos',
            'direccion',
            'num_telefono',
            'correo',
            'edad',
        )

        labels = {
            'cedula' : 'Cedula',
            'nombres' :'Nombres',
            'apellidos' : 'Apellidos',
            'direccion' : 'Direccion',
            'num_telefono' : 'Numero Celular',
            'correo' : 'Correo',
            'edad' : 'Edad',
        }
        widgets={
            'cedula' : forms.TextInput(attrs={'class':'form-control'}),
            'nombres' :forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'num_telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.EmailInput(attrs={'class':'form-control'}),
            'edad' : forms.TextInput(attrs={'class':'form-control'}),
        }
class medicoForm(forms.ModelForm):
    
    class Meta:
        model = medico
        fields = ("cedula",
            'nombres',
            'apellidos',
            'direccion',
            'num_telefono',
            'id_especialidad',
        )
        labels = {
            'cedula': 'Cedula',
            'nombres' : ' Nombres',
            'apellidos' : 'Apellidos',
            'direccion' : 'Direccion' , 
            'num_telefono ' : 'Numero Celular' , 
            'id_especialidad' : 'Especialidad'
        }
        widgets = {
            'cedula' : forms.TextInput(attrs={'class':'form-control'}) ,
            'nombres' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' :forms.TextInput(attrs={'class':'form-control'}) ,
            'direccion' :forms.TextInput(attrs={'class':'form-control'}) ,
            'num_telefono':forms.TextInput(attrs={'class':'form-control'}) ,
            'id_especialidad' : forms.Select(attrs={'class':'form-control'}), 

        }

class citaForm(forms.ModelForm):
    
    class Meta:
        model = cita
        fields = ("numero_cita",
            'fecha',
            'hora',
            'cliente_id',
            'medico_id',
        )
        labels = {
            'numero_cita' : 'No Cita' ,
            'fecha' : 'Fecha' ,
            'hora' : 'Hora' ,
            'cliente_id' : 'Cliente',
            'medico_id' : 'Medico',

        }

        widgets = {
            'numero_cita' : forms.TextInput(attrs={'class':'form-control'}),
            'cliente_id' : forms.Select(attrs={'class':'form-control'}),
            'medico_id' : forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}), 
            'hora':forms.TimeInput(attrs={'class':'form-control'}),
        }



