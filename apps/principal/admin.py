from django.contrib import admin
from .models import Alumno,Hospital,Cicloescolar,Atencion,Escuela
from .actions import export_as_excel
 

@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
	list_display = ('id','user','alumno','get_escolaridad','fecha','modified','atencion','fechaatencion','hospital','edad','meses',
		 'grado')
	search_fields = ('nombre',)
	list_filter = ('atencion','user','hospital','fechaatencion') 
	actions = [export_as_excel] 
 


	# asi se  obtiene un atributo del un pk order_file=tabla foranea, 
	def get_escolaridad(self, obj):
		return obj.alumno.escolaridad
	get_escolaridad.admin_order_field='alumno' #Allows column order sorting tabla  foranea
	get_escolaridad.short_description ='escolaridad' #Renames column head
 

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
	list_display = ('nombre','get_usuarios') 
	filter_horizontal = ('usuarios',)


@admin.register(Cicloescolar)
class CicloescolarAdmin(admin.ModelAdmin):
	list_display = ('descripcion','fechaini','fechafin','status')
 	
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','sexo','colonia','callenum','localidad','discapacidad','escolaridad','fechanaciomiento',)
	search_fields = ('id','nombre')

@admin.register(Escuela)
class EscualaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'colonia','direccion','localidad')
	search_fields = ('id', 'nombre')
