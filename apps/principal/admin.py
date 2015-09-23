from django.contrib import admin
from .models import Alumno,Hospital,Cicloescolar

from .actions import export_as_excel
 

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('user','folio','fecha','modified','atencion','fechaatencion','hospital','nombre','edad','meses','sexo','grado','escolaridad','escuela' )
	search_fields = ('nombre','folio')
	list_filter = ('escolaridad','atencion','user','hospital','fechaatencion') 
	actions = [export_as_excel] 



@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
	list_display = ('nombre','get_usuarios') 
	filter_horizontal = ('usuarios',)



@admin.register(Cicloescolar)
class CicloescolarAdmin(admin.ModelAdmin):
	list_display = ('descripcion','fechaini','fechafin','status')
 	
