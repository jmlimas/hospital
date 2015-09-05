
from django.conf.urls import url
from . import views 


urlpatterns = [
	url(r'^$',views.IndexView.as_view(),name='index'),    
	url(r'^addalumno/$',views.AddAlumnoViews.as_view(),name='add_alumno'),
	url(r'^updatealumno/(?P<pk>\d+)/$',views.UpdateAlumno.as_view(),name='alumno_update'),
	url(r'^listhoy/$',views.ListAlumnoshoy.as_view(),name='list_hoy'),
	url(r'^listhoyl/$',views.ListAlumnoshoyL.as_view(),name='list_hoyl'),
    url(r'^search/$',views.SerchAlumnoView.as_view(),name='buscar'),
    url(r'^lisdisg/$',views.ListaAlumnosDiscagomez.as_view(),name='list_discgom'),
    url(r'^lisPrimg/$',views.ListaAlumnosPrimagomez.as_view(),name='list_primgom'),
    url(r'^lispreeg/$',views.ListaAlumnosPreegomez.as_view(),name='list_preegom'),
    url(r'^listsecg/$',views.ListaAlumnosSecgomez.as_view(),name='list_secgom'),
    url(r'^listnoesyedadg/$',views.ListaAlumNoestytiedadg.as_view(),name='list_secgom'),
    url(r'^listalumbachg/$',views.ListaAlumbachg.as_view(),name='list_bachgom'),
    url(r'^listsinedadg/$',views.ListaSinEdadg.as_view(),name='list_sinedadgom'),

    url(r'^lisdisl/$',views.ListaAlumnosDiscal.as_view(),name='list_discler'),
    url(r'^lisPriml/$',views.ListaAlumnosPrimal.as_view(),name='list_primler'),
    url(r'^lispreel/$',views.ListaAlumnosPreel.as_view(),name='list_preeler'),
    url(r'^listsecl/$',views.ListaAlumnosSecl.as_view(),name='list_secler'),
    url(r'^listnoesyedadl/$',views.ListaAlumNoestytiedadl.as_view(),name='list_secler'),
    url(r'^listalumbachl/$',views.ListaAlumbachl.as_view(),name='list_bachler'),
    url(r'^listsinedadl/$',views.ListaSinEdadl.as_view(),name='list_sinedadler'),    

    url(r'^listPischoy/$',views.ListaAlumPishoy.as_view(),name='lis_piscohoy'),
    url(r'^lisdisp/$',views.ListaAlumnosDiscap.as_view(),name='list_disclep'),
    url(r'^lisPrimp/$',views.ListaAlumnosPrimap.as_view(),name='list_primlep'),
    url(r'^lispreep/$',views.ListaAlumnosPreep.as_view(),name='list_preelep'),
    url(r'^listsecp/$',views.ListaAlumnosSecp.as_view(),name='list_seclep'),
    url(r'^listnoesyedadp/$',views.ListaAlumNoestytiedadp.as_view(),name='list_seclep'),
    url(r'^listalumbachp/$',views.ListaAlumbachp.as_view(),name='list_bachlep'),  
    url(r'^listsinedadp/$',views.ListaSinEdadp.as_view(),name='list_sinedadp'),   

   

    url(r'^add/$', views.AddAl.as_view(),name='xx'),
    
    

 

]
  

