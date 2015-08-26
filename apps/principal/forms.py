#encoding:utf-8
from django import forms
from models import Alumno    
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class AddAlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		exclude = ['ciclo','folio','user',] 
        #fechaatencion = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
        widgets = {
                    'observacion': forms.Textarea(attrs={'placeholder':'observacion','rows':'4','cols': '40'}),
                    'nombre': forms.TextInput(attrs={'placeholder':'Nombre Alumno','size': '40'}),
                    'escuela': forms.TextInput(attrs={'placeholder':'Nombre de escuela','size': '40'}),
                    'edad': forms.NumberInput(attrs={'placeholder':'Edad','min': '0', 'max': '19'}),
                    'coloniaal': forms.TextInput(attrs={'placeholder':'Colonia alumno','size': '40'}),
                    'callenumal': forms.TextInput(attrs={'placeholder':'Calle y numero alumno','size': '40'}),
                    'localidadal': forms.TextInput(attrs={'placeholder':'Localidades alumno','size': '40'}),
                    'meses': forms.NumberInput(attrs={'placeholder':'Meses','min': '0', 'max': '11'}), 
                    'coloniaesc': forms.TextInput(attrs={'placeholder':'Colonia escuela','size': '40'}),
                    'direccionesc': forms.TextInput(attrs={'placeholder':'Direccion escuela','size': '40'}),
                    'localidadesc': forms.TextInput(attrs={'placeholder':'Localidades escuela','size': '40'}),
                    'grado': forms.NumberInput(attrs={'placeholder': 'Grado','min': '0', 'max':'6'}),              
                    'especialidad': forms.TextInput(attrs={'placeholder':'Especialidad','size': '40'}),
                    'diagnostico': forms.TextInput(attrs={'placeholder':'Diagnostico','size': '40'}),
                    'tema': forms.TextInput(attrs={'placeholder':'Tema','size': '40'}), 
                    'fechaatencion':forms.TextInput(attrs={'placeholder':'aaaa-mm-dd'}),  
                }   
 
 
class AddAlumnoFormxxx(forms.Form):
    date_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    time = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))
