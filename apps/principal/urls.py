
from django.conf.urls import url
from . import views 


urlpatterns = [
	#url(r'^$',views.IndexView.as_view(),name='index'),   
	url(r'^$', "apps.users.views.inicio"),	
	url(r'^addescuela/$',views.AddEscuela.as_view(),name='add_escuela'),
	url(r'^addalumno/$',views.AddAlumno.as_view(),name='add_alumno'),  
	url(r'^listalumno/$',views.ListAlumnos.as_view(),name='list_alumno'),  
    url(r'^expatenciones/$', 'apps.principal.views.ExportaAtenciones',name='xds'), 
    url(r'^addaten/$',views.AddAtencionViews.as_view(),name='add_atencio'),
    url(r'^buscanombre_url/$','apps.principal.views.ListaAlumnos_ajax',name='aj_busanombre'),
    url(r'^auto/$','apps.principal.views.persona_auto_complete', name='persona_auto_complete'),
    url(r'^auto_escuela/$','apps.principal.views.escuela_auto_completa', name='escuela_auto_complete'),
    url(r'^addalu_modal/$','apps.principal.views.addalumodel',name='add_alumnomodel'),
    url(r'^edad_alumno/$','apps.principal.views.edad_alumno_ajax'),
   
]
  

