#encoding:utf-8
from django import forms
from models import Alumno,Atencion,Escuela  

 

#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


class AddAtencionForm(forms.ModelForm):
	class Meta:
		model = Atencion
		exclude = ['ciclo','user'] 

        persona_display = forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de alumno','size': '40','class':'form-control'}))
        observacion = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols': '40'})) 
        grado = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Grado','min': '0', 'max':'6'}))
        especialidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Especialidad','size': '40'}))
        diagnostico = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Diagnostico','size': '40'}))
        tema = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tema','size': '40'}))
        horainicio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hh:mm:ss'}))
        #horainicio = forms.TimeField(widget=TimeWidget)
        horafin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hh:mm:ss'}))
        fechaatencion = forms.DateField(('%Y/%d/%Y',), 
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'class':'datePicker', 
            'size':'10'
        })
    )
         
        def __init__(self, *args, **kwargs):
                super(AddAtencionForm, self).__init__(*args, **kwargs)
                self.fields['persona_display'].label = "Autor"
                self.fields['alumno'].widget = forms.HiddenInput(attrs={'class':'form-control'}) # apago el  combo del cliente para que no se vea. :)
 
 


class AlumnoForm(forms.ModelForm):
        class Meta:
                model = Alumno
                exclude = ['user']

        nombreAlumno = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre Alumno','size': '60'}))
        coloniaal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Colonia alumno','size': '40'}))
        callenumal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Calle y numero alumno','size': '40'}))
        localidadal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Localidades alumno','size': '40'}))
        escuela_display = forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de Escuela','size': '20','class':'form-control'}))
  

        def __init__(self, *args, **kwargs):
            super(AlumnoForm, self).__init__(*args, **kwargs)
            self.fields['escuela_display'].label = "Autor"
           # self.fields['escuela'].widget = forms.HiddenInput(attrs={'class':'form-control'}) # apago el  combo del cliente para que no se vea. :)
 


class AddEscuelaForm(forms.ModelForm):
        class Meta:
            model = Escuela
            exclude = ['user']
        
        colonia = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Colonia escuela','size': '40'}))
        direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Direccion escuela','size': '40'}))
        localidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Localidades escuela','size': '40'}))

       
     
        
class LoginForm(forms.Form):

    username = forms.CharField(max_length=30, 
                widget = forms.TextInput(attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa un nombre de usuario'
                    }))
    password = forms.CharField(max_length=30,
                widget = forms.TextInput(attrs = {
                    'type' : 'password',
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa su contraseña'
                    }))

 