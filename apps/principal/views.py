# -*- coding: utf-8 -*-
from django.views.generic import  TemplateView,FormView,ListView,UpdateView 
from braces.views import LoginRequiredMixin,GroupRequiredMixin
from .models import Alumno,Cicloescolar
from .forms  import AddAlumnoForm 
from django.shortcuts import get_object_or_404 

from datetime import date 
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
 

class IndexView(TemplateView):
	template_name = 'principal/index.html'	

	def get_context_data(self, **kwargs):
		today = date.today()	
		print today 
		context = super(IndexView,self).get_context_data(**kwargs)
		#context['alum3'] = Alumno.objects.all().order_by('-fecha')[:3]
		#Gomez
		
		context['pre_g'] = Alumno.objects.filter(escolaridad='Preescolar',hospital=1,ciclo__status=True).count()
		context['prim_g'] = Alumno.objects.filter(escolaridad='Primaria',hospital=1,ciclo__status=True).count()		 
		context['sec_g'] = Alumno.objects.filter(escolaridad='Secundaria',hospital=1,ciclo__status=True).count()
		context['ne_g'] = Alumno.objects.filter(escolaridad='No Estudia y tiene edad escolar',hospital=1,ciclo__status=True).count()		 
		context['disc_g'] = Alumno.objects.filter(hospital=1,ciclo__status=True).exclude(discapacidad='No').count()
		context['bach_g'] = Alumno.objects.filter(escolaridad='Bachillerato',hospital=1,ciclo__status=True).count()
		context['sinedadesc_g'] = Alumno.objects.filter(escolaridad='No Tiene Edad escolar',hospital=1,ciclo__status=True).count()
		context['solohoy_g'] = Alumno.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,hospital=1).count()
		context['pedhoy_g'] = Alumno.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1,modalidad='Pediatria').count()
		context['exthoy_g'] = Alumno.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1,modalidad='ConsultaExt').count()
		context['domhoy_g'] = Alumno.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1,modalidad='AtencionDom').count()
		context['pedhoy_l'] = Alumno.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=2,modalidad='Pediatria').count()
		context['exthoy_l'] = Alumno.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=2,modalidad='ConsultaExt').count()		
		context['pre_l'] = Alumno.objects.filter(escolaridad='Preescolar',fecha__year=today.year,fecha__month=today.month,hospital=2).count()
		context['prim_l'] = Alumno.objects.filter(escolaridad='Primaria',fecha__year=today.year,fecha__month=today.month,hospital=2).count()
		context['sec_l'] = Alumno.objects.filter(escolaridad='Secundaria',fecha__year=today.year,fecha__month=today.month,hospital=2).count()
		context['ne_l'] = Alumno.objects.filter(escolaridad='No Estudia y tiene edad escolar',fecha__year=today.year,fecha__month=today.month,hospital=2).count()		 
		context['disc_l'] = Alumno.objects.filter(discapacidad='Discapacidad',fecha__year=today.year,fecha__month=today.month,hospital=2).count()
		context['bach_l'] = Alumno.objects.filter(escolaridad='Bachillerato',fecha__year=today.year,fecha__month=today.month,hospital=2).count()
		context['sinedadesc_l'] = Alumno.objects.filter(escolaridad='No Tiene Edad escolar',fecha__year=today.year,fecha__month=today.month,hospital=2).count()
		context['solohoy_l'] = Alumno.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,hospital=2).count()

		return context
 
  
class AddAlumnoViews(LoginRequiredMixin,FormView):
	form_class = AddAlumnoForm
	template_name = 'principal/addalumno.html'
	model = Alumno
	success_url = '/'

	def form_valid(self, form, *args, **kwargs): 
 		xfolio =  Alumno.objects.count()+1
 		xciclo = Cicloescolar.objects.get(status=True)
 		form.instance.ciclo = xciclo 
		form.instance.folio = xfolio
		form.instance.user = self.request.user	 
		form.save()
 		return super(AddAlumnoViews, self).form_valid(form)

 	def form_invalid(self,form):
 		print 'NO'
 		return super(AddAlumnoViews,self).form_invalid(form)


class ListAlumnoshoy(LoginRequiredMixin,GroupRequiredMixin,ListView):
	context_object_name = 'alumnos'
	template_name = 'principal/listalumnoshoy.html'
	model = Alumno
	group_required = ['gomez','super']


	def get_queryset(self):
		today = date.today()
		return super(ListAlumnoshoy, self).get_queryset().filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1) 


	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListAlumnoshoy, self).get_context_data(**kwargs)		 
		context['hospital'] = "Gomez Palacio"
		context['ciclo'] = Cicloescolar.objects.filter(status=True)
		return context

class ListAlumnoshoyL(LoginRequiredMixin,GroupRequiredMixin,ListView):
	context_object_name = 'alumnos'
	template_name = 'principal/listalumnoshoy.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):
		today = date.today()
		return super(ListAlumnoshoyL, self).get_queryset().filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=2) 


	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListAlumnoshoyL, self).get_context_data(**kwargs)		 
		context['hospital'] = "Hospital de Lerdo"
		context['ciclo'] = Cicloescolar.objects.filter(status=True)
		return context


class ListaAlumnosDiscagomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Discapacidad acumulado Gomez
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']


	def get_queryset(self):	
		return super(ListaAlumnosDiscagomez,self).get_queryset().filter(hospital=1,ciclo__status=True).exclude(discapacidad='No') 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumnosDiscagomez, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos con Discapacidad Gomez Palacio" 
		return context

class ListaAlumnosPrimagomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Primaria Gomez Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']

	def get_queryset(self):	
		return super(ListaAlumnosPrimagomez,self).get_queryset().filter(escolaridad='Primaria',hospital=1,ciclo__status=True) 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumnosPrimagomez, self).get_context_data(**kwargs)	 
		context['hospital'] = "Concentrado de Alumnos Primaria Gomez Palacio"	
		return context

class ListaAlumnosPreegomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Prescolar Gomez Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']

	def get_queryset(self):	
		return super(ListaAlumnosPreegomez,self).get_queryset().filter(escolaridad='Preescolar',hospital=1,ciclo__status=True) 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumnosPreegomez, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos Preescolar Gomez Palacio"		 
		return context

class ListaAlumnosSecgomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Secundaria Gomez Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']

	def get_queryset(self):	
		return super(ListaAlumnosSecgomez,self).get_queryset().filter(escolaridad='Secundaria',hospital=1,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumnosSecgomez, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos Secundaria Gomez Palacio"		 
		return context

class ListaAlumNoestytiedadg(LoginRequiredMixin,GroupRequiredMixin,ListView): # No estudia y tiene edad escalar Gomez Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']

	def get_queryset(self):	
		return super(ListaAlumNoestytiedadg,self).get_queryset().filter(escolaridad='No Estudia y tiene edad escolar',hospital=1,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumNoestytiedadg, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos que No estudia y tiene edad escalar Gomez Palacio"		 
		return context

class ListaAlumbachg(LoginRequiredMixin,GroupRequiredMixin,ListView): # Bachillerato Gomez Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']

	def get_queryset(self):	
		return super(ListaAlumbachg,self).get_queryset().filter(escolaridad='Bachillerato',hospital=1,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumbachg, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos Bachillerato Gomez Palacio"		 
		return context


class ListaSinEdadg(LoginRequiredMixin,GroupRequiredMixin,ListView): # Sin Edad Gomez Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['gomez','super']

	def get_queryset(self):	
		return super(ListaSinEdadg,self).get_queryset().filter(escolaridad='No Tiene Edad escolar',hospital=1,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaSinEdadg, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos No Tiene Edad escolar Gomez Palacio"		 
		return context

## Lerdo

class ListaAlumnosDiscal(LoginRequiredMixin,GroupRequiredMixin,ListView): # Discapacidad acumulado lerdo
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaAlumnosDiscal,self).get_queryset().filter(hospital=2,ciclo__status=True).exclude(discapacidad='No') 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumnosDiscal, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos con Discapacidad Lerdo" 
		return context

class ListaAlumnosPrimal(LoginRequiredMixin,GroupRequiredMixin,ListView): # Primaria lerdo Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaAlumnosPrimal,self).get_queryset().filter(escolaridad='Primaria',hospital=2,ciclo__status=True) 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumnosPrimal, self).get_context_data(**kwargs)	 
		context['hospital'] = "Concentrado de Alumnos Primaria Lerdo"	
		return context

class ListaAlumnosPreel(LoginRequiredMixin,GroupRequiredMixin,ListView): # Prescolar lerdo Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaAlumnosPreel,self).get_queryset().filter(escolaridad='Preescolar',hospital=2,ciclo__status=True) 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumnosPreel, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos Preescolar Lerdo"		 
		return context

class ListaAlumnosSecl(LoginRequiredMixin,GroupRequiredMixin,ListView): # Secundaria lerdo Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaAlumnosSecl,self).get_queryset().filter(escolaridad='Secundaria',hospital=2,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumnosSecl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos Secundaria Lerdo"		 
		return context

class ListaAlumNoestytiedadl(LoginRequiredMixin,GroupRequiredMixin,ListView): # No estudia y tiene edad escalar lerdo Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaAlumNoestytiedadl,self).get_queryset().filter(escolaridad='No Estudia y tiene edad escolar',hospital=2,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumNoestytiedadl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos que No estudia y tiene edad escalar Lerdo"		 
		return context

class ListaAlumbachl(LoginRequiredMixin,GroupRequiredMixin,ListView): # Bachillerato lerdo Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaAlumbachl,self).get_queryset().filter(escolaridad='Bachillerato',hospital=2,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumbachl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos Bachillerato Lerdo"		 
		return context


class ListaSinEdadl(LoginRequiredMixin,GroupRequiredMixin,ListView): # Sin Edad lerdo Acumulado
	context_object_name = 'alumnos'
	template_name = 'principal/alumnosxx.html'
	model = Alumno
	group_required = ['lerdo','super']

	def get_queryset(self):	
		return super(ListaSinEdadl,self).get_queryset().filter(escolaridad='No Tiene Edad escolar',hospital=2,ciclo__status=True) 

	def get_context_data(self, **kwargs):  
		context = super(ListaSinEdadl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Alumnos No Tiene Edad escolar Lerdo"		 
		return context

 

class UpdateAlumno(UpdateView):
	template_name = 'principal/addalumno.html'
	model = Alumno
	form_class = AddAlumnoForm
	success_url = reverse_lazy('principal_app:list_hoy')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateAlumno, self).form_valid(form)
 

class SerchAlumnoView(LoginRequiredMixin,GroupRequiredMixin,ListView):
	model = Alumno
	template_name = 'principal/buscaalumno.html' 
	group_required = ['super']
	

	def get_queryset(self):
		search_query = self.request.GET.get('q',None)
		if search_query:
			queryset = super(SerchAlumnoView, self).get_queryset().all()  
		else:
			queryset = ""
			
		q = self.request.GET.get('q', '') 
		print "sesta es el valor de :" +q
				
		if q:
		    queryset = queryset.filter(
		        Q(escuela__icontains=q)|
		        Q(nombre__icontains=q) 
		    )		
		return queryset