#encoding:utf-8
from django import forms
from models import Alumno    

class AddAlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		exclude = ['ciclo','folio','user'] 
        observacion = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols': '40'})) 
        nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre Alumno','size': '40'}))
        escuela = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de escuela','size': '40'}))
        edad = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Edad','min': '0', 'max': '19'}))
        coloniaal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Colonia alumno','size': '40'}))
        callenumal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Calle y numero alumno','size': '40'}))
        localidadal = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Localidades alumno','size': '40'}))
        meses = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Meses','min': '0', 'max': '11'}))
        coloniaesc = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Colonia escuela','size': '40'}))
        direccionesc = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Direccion escuela','size': '40'}))
        localidadesc = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Localidades escuela','size': '40'}))
        grado = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Grado','min': '0', 'max':'6'}))
        especialidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Especialidad','size': '40'}))
        diagnostico = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Diagnostico','size': '40'}))
        tema = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tema','size': '40'}))
        fechaatencion = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'aaaa-mm-dd'}))
        horainicio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hh:mm:ss'}))
        horafin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hh:mm:ss'}))
       
                  
               