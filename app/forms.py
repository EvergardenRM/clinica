from django import forms
from app.models import *

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

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
            'usuario_id',
            'especializacion_id'
        )
        labels = {
            'numero_cita' : 'No Cita' ,
            'fecha' : 'Fecha' ,
            'hora' : 'Hora' ,
            'cliente_id' : 'Cliente',
            'medico_id' : 'Medico',
            'usuario_id': 'Usuario',
            'especializacion_id' : 'Especialidad' ,

        }

        widgets = {
            'numero_cita' : forms.TextInput(attrs={'class':'form-control'}),
            'cliente_id' : forms.Select(attrs={'class':'form-control'}),
            'medico_id' : forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}), 
            'hora':forms.TimeInput(attrs={'class':'form-control'}),
            'usuario_id': forms.Select(attrs={'class':'form-control'}),
            'especializacion_id' : forms.Select(attrs={'class':'form-control'}),
        }



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth')
        labels = {
            'username' : 'Username',
            'email' : 'Email',
            'date_of_birth': 'Fecha Nacimiento',
            
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
#admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)
class RolForm(forms.ModelForm):
    
    class Meta:
        model = Rol
        fields = ("nombre",)
        labels = {
            'nombre' : 'Rol',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
        }


class Rol_UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Rol_Usuario
        fields = ("usuario",
            'rol',
        )
        labels = {
            'rol' : 'Rol',
            'usuario' : 'Usuario',
        }
        widgets = {
            'rol' : forms.Select(attrs={'class':'form-control'}),
            'usuario' : forms.Select(attrs={'class':'form-control'}),
        }
