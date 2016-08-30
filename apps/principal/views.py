# -*- coding: utf-8 -*-
from django.views.generic import  TemplateView,FormView,ListView,UpdateView,CreateView
from braces.views import LoginRequiredMixin,GroupRequiredMixin
from .models import Atencion,Cicloescolar,Hospital,Alumno,Escuela
from .forms  import AddAtencionForm,AlumnoForm,AddEscuelaForm,LoginForm
from django.db.models import Count 

from django.db import connection
from datetime import date 
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
 
from django.http import HttpResponse,Http404,JsonResponse
#from django.core import serializers 
import json
import json as simplejson
import csv

from django.core import serializers

class IndexView(TemplateView):
	template_name = 'principal/index.html'	

class IndexView(TemplateView):
	template_name = 'principal/index.html'	

	def get_context_data(self, **kwargs):
		today = date.today()	
		context = super(IndexView,self).get_context_data(**kwargs)
		
		context['solohoy_g'] = Atencion.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,hospital=1).count()
		context['pedhoy_g'] = Atencion.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1,modalidad='Pediatria').count()
		context['exthoy_g'] = Atencion.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1,modalidad='ConsultaExt').count()
		context['domhoy_g'] = Atencion.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=1,modalidad='AtencionDom').count()
		context['pedhoy_l'] = Atencion.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=2,modalidad='Pediatria').count()
		context['exthoy_l'] = Atencion.objects.filter(fecha__year=today.year,
			fecha__month=today.month,fecha__day=today.day,hospital=2,modalidad='ConsultaExt').count()	
		context['solohoy_l'] = Atencion.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,hospital=2).count()
		context['pisco_hoy'] = Atencion.objects.filter(atencion='Psicologia',fecha__year=today.year,fecha__month=today.month,fecha__day=today.day).count()
		


		context['pre_g'] = Atencion.objects.filter(alumno__escolaridad='Preescolar',hospital=1,ciclo__status=True).count()
		context['prim_g'] = Atencion.objects.filter(alumno__escolaridad='Primaria',hospital=1,ciclo__status=True).count()		 
		context['sec_g'] = Atencion.objects.filter(alumno__escolaridad='Secundaria',hospital=1,ciclo__status=True).count()
		context['ne_g'] = Atencion.objects.filter(alumno__escolaridad='No Estudia y tiene edad escolar',hospital=1,ciclo__status=True).count()		 
		context['disc_g'] = Atencion.objects.filter(hospital=1,ciclo__status=True).exclude(alumno__discapacidad='No').count()
		context['bach_g'] = Atencion.objects.filter(alumno__escolaridad='Bachillerato',hospital=1,ciclo__status=True).count()
		context['sinedadesc_g'] = Atencion.objects.filter(alumno__escolaridad='No Tiene Edad escolar',hospital=1,ciclo__status=True).count()
			
		context['pre_l'] = Atencion.objects.filter(alumno__escolaridad='Preescolar',hospital=2,ciclo__status=True).count()
		context['prim_l'] = Atencion.objects.filter(alumno__escolaridad='Primaria',hospital=2,ciclo__status=True).count()
		context['sec_l'] = Atencion.objects.filter(alumno__escolaridad='Secundaria',hospital=2,ciclo__status=True).count()
		context['ne_l'] = Atencion.objects.filter(alumno__escolaridad='No Estudia y tiene edad escolar',hospital=2,ciclo__status=True).count()		 
		context['disc_l'] = Atencion.objects.filter(hospital=2,ciclo__status=True).exclude(alumno__discapacidad='No').count()
		context['bach_l'] = Atencion.objects.filter(alumno__escolaridad='Bachillerato',hospital=2,ciclo__status=True).count()
		context['sinedadesc_l'] = Atencion.objects.filter(alumno__escolaridad='No Tiene Edad escolar',hospital=2,ciclo__status=True).count()
		
		context['pre_p'] = Atencion.objects.filter(alumno__escolaridad='Preescolar',atencion='Psicologia',ciclo__status=True).count()
		context['prim_p'] = Atencion.objects.filter(alumno__escolaridad='Primaria',atencion='Psicologia',ciclo__status=True).count()
		context['sec_p'] = Atencion.objects.filter(alumno__escolaridad='Secundaria',atencion='Psicologia',ciclo__status=True).count()
		context['ne_p'] = Atencion.objects.filter(alumno__escolaridad='No Estudia y tiene edad escolar',atencion='Psicologia',ciclo__status=True).count()		 
		context['disc_p'] = Atencion.objects.filter(ciclo__status=True,atencion='Psicologia').exclude(alumno__discapacidad='No').count()
		context['bach_p'] = Atencion.objects.filter(alumno__escolaridad='Bachillerato',atencion='Psicologia',ciclo__status=True).count()
		context['sinedadesc_p'] = Atencion.objects.filter(alumno__escolaridad='No Tiene Edad escolar',atencion='Psicologia',ciclo__status=True).count()
	
         

		# Graficas 
		#context['dd'] = Atencion.objects.values_list('nombre').order_by('nombre','id').distinct('nombre') ## quita los nombres duplicados
		#context['dd'] = Atencion.objects.order_by('nombre','id').distinct('nombre')  ##quita los duplicados

		#context['ddz'] = (Atencion.objects.filter(ciclo__status=True).values('nombre').annotate(id = Min('id')).order_by('nombre', 'id')) # quita nombres duplicados optiene el menor id  pero presenta una lista

		#context['dd'] = Atencion.objects.filter(ciclo__status=True,atencion='Pedagogia').order_by('nombre', 'id').distinct('nombre') ## Este es el bueno esta es la base
		#print context['dd']		 
			
		#cursor.execute('select user_id,count(user_id) FROM public.principal_Atencion group  by user_id'),
		#xx = Atencion.objects.raw('select id,user_id as Maestra,count(user_id) as total FROM public.principal_Atencion group  by id,user_id')
 		cursor = connection.cursor()
 		
		 
		 #### Procesa los Atencions atenididos  por Maestras y alunos  no deuplicados  y  selecciona el 
		 #### Primer Atencion atenido por la  maestra es decir el id mas viejo o chioco o minimo
		wf = ('No Estudia y tiene edad escolar','No Tiene Edad escolar')
		cursor.execute("SELECT DISTINCT ON (d.nombre)  b.username,a.id,d.nombre into ped \
		FROM principal_Atencion a  \
		join users_user b ON  a.user_id = b.id \
		join principal_cicloescolar c ON c.id = a.ciclo_id \
		join principal_Alumno d on d.id = a.alumno_id \
		WHERE atencion='Pedagogia' and c.status=true and d.escolaridad not in  %s \
		order by d.nombre,a.id",[wf])


 		cursor.execute("Select a.username as user__username,count(a.id) as total from ped a group by user__username order by total desc")
		columns = [column[0] for column in cursor.description]
		res_ped  = []
		for row in cursor.fetchall():
			res_ped.append(dict(zip(columns,row)))			
			# abajo en la  linia 112 los junta el resultado de la Maestra con el de la psicologa y lo agrega el context['productividad']

 		#### Procesa los Atencions atenididos por Psicologia y alunos  no deuplicados  y  selecciona el 
		#### Primer Atencion atenido por la  Psicologia es decir el id mas viejo o chioco o minimo
		wf = ('No Estudia y tiene edad escolar','No Tiene Edad escolar')
		cursor.execute("SELECT DISTINCT ON (d.nombre)  b.username,a.id,d.nombre into Pis \
		FROM principal_Atencion a  \
		join users_user b ON  a.user_id = b.id \
		join principal_cicloescolar c ON c.id = a.ciclo_id \
		join principal_Alumno d on d.id = a.alumno_id \
		WHERE atencion ='Psicologia' and c.status=true and d.escolaridad not in  %s \
		order by d.nombre,a.id",[wf])


 		cursor.execute("Select a.username as user__username,count(a.id) as total from Pis a group by user__username order by total desc")
		columns = [column[0] for column in cursor.description]
		res_psic = []
		for row in cursor.fetchall():
			res_psic.append(dict(zip(columns,row)))			

		context['productividad'] = res_ped+res_psic
		cursor.execute("drop table ped");
		cursor.execute("drop table Pis");
		cursor.close() 
		 
 

		
		#context['productividad'] = Atencion.objects.filter(ciclo__status=True,).exclude(
		#	escolaridad__icontains='No Tiene Edad escolar').filter(ciclo__status=True).exclude(escolaridad__icontains = 'No Estudia y tiene edad escolar'
		#	).values('user__username').annotate(total=Count('nombre',distinct=True)).order_by('-total')

		#print context['productividad'] 
		
   		q =  Atencion.objects.filter(ciclo__status=True).exclude(
   			atencion__icontains='Psicologia').values('alumno__escolaridad').annotate(total=Count('alumno',distinct=True)).order_by('-total')
		context['itens'] = q

		#atencion por nivel todo el ciclo 
		#q =  Atencion.objects.values('escolaridad').annotate(
		#	total=Count('escolaridad')).order_by('escolaridad').values('escolaridad','total')
		#context['itens'] = q
 		#print context['itens']  	
 		
 		context['hosp'] = Atencion.objects.filter(ciclo__status=True).exclude(
			alumno__escolaridad__icontains='No Tiene Edad escolar').filter(ciclo__status=True).exclude(alumno__escolaridad__icontains = 'No Estudia y tiene edad escolar'
			).filter(ciclo__status=True).exclude(atencion='Psicologia').filter(ciclo__status=True
			).values('hospital__nombre').annotate(total=Count('alumno',distinct=True)).order_by('-total')
 		return context
 		 
 		 
 
class AddEscuela(CreateView):
	form_class = AddEscuelaForm
	template_name = 'principal/addEscuela.html'
	model = Escuela
	success_url = '/'
	

class AddAl(CreateView):
	form_class = AddAtencionForm
	template_name = 'principal/addAtencion3333.html'
	model = Atencion
	success_url = '/'


class AddAtencionViews(LoginRequiredMixin,CreateView):
	form_class = AddAtencionForm
	template_name = 'principal/addAtencion.html'
	model = Atencion	
	success_url = '/'

	def get_form(self, form_class):
		#print self.request.user.id
		form = super(AddAtencionViews, self).get_form(form_class)
		form.fields['hospital'].queryset = Hospital.objects.filter(usuarios__pk= self.request.user.id)
		return form
  

	def form_valid(self, form, *args, **kwargs): 
 		xciclo = Cicloescolar.objects.get(status=True)
 		form.instance.ciclo = xciclo 
		form.instance.user = self.request.user	 
		form.save()
 		return super(AddAtencionViews, self).form_valid(form)

 	def form_invalid(self,form): 		
 		return super(AddAtencionViews,self).form_invalid(form)


class ListAtencionshoy(LoginRequiredMixin,GroupRequiredMixin,ListView):
	context_object_name = 'Atencions'
	template_name = 'principal/listAtencionshoy.html'
	model = Atencion
	group_required = ['gomez','super']

																	 

	def get_queryset(self):
		today = date.today()
		if self.request.user.is_superuser:
			return super(ListAtencionshoy, self).get_queryset().filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,hospital=1) 
		else:
		   	return super(ListAtencionshoy, self).get_queryset().filter(user=self.request.user,fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,hospital=1) 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListAtencionshoy, self).get_context_data(**kwargs)		 
		context['hospital'] = "Gomez Palacio"
		context['ciclo'] = Cicloescolar.objects.filter(status=True)
		return context



class ListAtencionshoyL(LoginRequiredMixin,GroupRequiredMixin,ListView):
	context_object_name = 'Atencions'
	template_name = 'principal/listAtencionshoy.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):
		today = date.today()
		if self.request.user.is_superuser:
			return super(ListAtencionshoyL, self).get_queryset().filter(fecha__year=today.year,
				fecha__month=today.month,fecha__day=today.day,hospital=2)
		else:
			return super(ListAtencionshoyL, self).get_queryset().filter(user=self.request.user,fecha__year=today.year,
				fecha__month=today.month,fecha__day=today.day,hospital=2)		 	 


	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListAtencionshoyL, self).get_context_data(**kwargs)		 
		context['hospital'] = "Hospital de Lerdo"
		context['ciclo'] = Cicloescolar.objects.filter(status=True)
		return context


class ListaAtencionsDiscagomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Discapacidad acumulado Gomez
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']


	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsDiscagomez,self).get_queryset().filter(hospital=1,ciclo__status=True).exclude(discapacidad='No').order_by('folio') 
		else:
			return super(ListaAtencionsDiscagomez,self).get_queryset().filter(user=self.request.user,hospital=1,ciclo__status=True).exclude(discapacidad='No').order_by('folio') 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsDiscagomez, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions con Discapacidad Gomez Palacio" 
		return context

class ListaAtencionsPrimagomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Primaria Gomez Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsPrimagomez,self).get_queryset().filter(escolaridad='Primaria',hospital=1,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionsPrimagomez,self).get_queryset().filter(user=self.request.user,escolaridad='Primaria',hospital=1,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsPrimagomez, self).get_context_data(**kwargs)	 
		context['hospital'] = "Concentrado de Atencions Primaria Gomez Palacio"	
		return context

class ListaAtencionsPreegomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Prescolar Gomez Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsPreegomez,self).get_queryset().filter(escolaridad='Preescolar',hospital=1,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionsPreegomez,self).get_queryset().filter(user=self.request.user,escolaridad='Preescolar',hospital=1,ciclo__status=True).order_by('folio')
	
	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsPreegomez, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Preescolar Gomez Palacio"		 
		return context

class ListaAtencionsSecgomez(LoginRequiredMixin,GroupRequiredMixin,ListView): # Secundaria Gomez Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsSecgomez,self).get_queryset().filter(escolaridad='Secundaria',hospital=1,ciclo__status=True).order_by('folio') 
		else:
			return super(ListaAtencionsSecgomez,self).get_queryset().filter(user=self.request.user,escolaridad='Secundaria',hospital=1,ciclo__status=True).order_by('folio') 

	def get_context_data(self, **kwargs):  
		context = super(ListaAtencionsSecgomez, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Secundaria Gomez Palacio"		 
		return context

class ListaAtencionestytiedadg(LoginRequiredMixin,GroupRequiredMixin,ListView): # No estudia y tiene edad escalar Gomez Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']

	def get_queryset(self):
		if self.request.user.is_superuser:	
			return super(ListaAtencionestytiedadg,self).get_queryset().filter(escolaridad='No Estudia y tiene edad escolar',hospital=1,ciclo__status=True).order_by('folio') 
		else:
			return super(ListaAtencionestytiedadg,self).get_queryset().filter(user=self.request.user,escolaridad='No Estudia y tiene edad escolar',hospital=1,ciclo__status=True).order_by('folio') 

	def get_context_data(self, **kwargs):  
		context = super(ListaAtencionestytiedadg, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions que No estudia y tiene edad escalar Gomez Palacio"		 
		return context

class ListaAlumbachg(LoginRequiredMixin,GroupRequiredMixin,ListView): # Bachillerato Gomez Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']

	def get_queryset(self):
		if self.request.user.is_superuser:
			return super(ListaAlumbachg,self).get_queryset().filter(escolaridad='Bachillerato',hospital=1,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAlumbachg,self).get_queryset().filter(user=self.request.user,escolaridad='Bachillerato',hospital=1,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumbachg, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Bachillerato Gomez Palacio"		 
		return context


class ListaSinEdadg(LoginRequiredMixin,GroupRequiredMixin,ListView): # Sin Edad Gomez Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['gomez','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaSinEdadg,self).get_queryset().filter(escolaridad='No Tiene Edad escolar',hospital=1,ciclo__status=True).order_by('folio') 
		else:
			return super(ListaSinEdadg,self).get_queryset().filter(user=self.request.user,escolaridad='No Tiene Edad escolar',hospital=1,ciclo__status=True).order_by('folio') 

	def get_context_data(self, **kwargs):  
		context = super(ListaSinEdadg, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions No Tiene Edad escolar Gomez Palacio"		 
		return context

## Lerdo

class ListaAtencionsDiscal(LoginRequiredMixin,GroupRequiredMixin,ListView): # Discapacidad acumulado lerdo
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsDiscal,self).get_queryset().filter(hospital=2,ciclo__status=True).exclude(discapacidad='No').order_by('folio')
		else:
			return super(ListaAtencionsDiscal,self).get_queryset().filter(user=self.request.user,hospital=2,ciclo__status=True).exclude(discapacidad='No').order_by('folio')

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsDiscal, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions con Discapacidad Lerdo" 
		return context

class ListaAtencionsPrimal(LoginRequiredMixin,GroupRequiredMixin,ListView): # Primaria lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsPrimal,self).get_queryset().filter(escolaridad='Primaria',hospital=2,ciclo__status=True).order_by('folio') 
		else:
			return super(ListaAtencionsPrimal,self).get_queryset().filter(escolaridad='Primaria',hospital=2,ciclo__status=True,user = self.request.user).order_by('folio') 


	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsPrimal, self).get_context_data(**kwargs)	 
		context['hospital'] = "Concentrado de Atencions Primaria Lerdoxxx"	
		return context

class ListaAtencionsPreel(LoginRequiredMixin,GroupRequiredMixin,ListView): # Prescolar lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsPreel,self).get_queryset().filter(escolaridad='Preescolar',hospital=2,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionsPreel,self).get_queryset().filter(user = self.request.user,escolaridad='Preescolar',hospital=2,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsPreel, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Preescolar Lerdo"		 
		return context

class ListaAtencionsSecl(LoginRequiredMixin,GroupRequiredMixin,ListView): # Secundaria lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsSecl,self).get_queryset().filter(escolaridad='Secundaria',hospital=2,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionsSecl,self).get_queryset().filter(user=self.request.user,escolaridad='Secundaria',hospital=2,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs):  
		context = super(ListaAtencionsSecl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Secundaria Lerdo"		 
		return context

class ListaAtencionestytiedadl(LoginRequiredMixin,GroupRequiredMixin,ListView): # No estudia y tiene edad escalar lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionestytiedadl,self).get_queryset().filter(escolaridad='No Estudia y tiene edad escolar',hospital=2,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionestytiedadl,self).get_queryset().filter(user=self.request.user,escolaridad='No Estudia y tiene edad escolar',hospital=2,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs):  
		context = super(ListaAtencionestytiedadl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions que No estudia y tiene edad escalar Lerdo"		 
		return context


class ListaAlumbachl(LoginRequiredMixin,GroupRequiredMixin,ListView): # Bachillerato lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAlumbachl,self).get_queryset().filter(escolaridad='Bachillerato',hospital=2,ciclo__status=True).order_by('folio') 
		else:
			return super(ListaAlumbachl,self).get_queryset().filter(user=self.request.user,escolaridad='Bachillerato',hospital=2,ciclo__status=True).order_by('folio') 

	def get_context_data(self, **kwargs):  
		context = super(ListaAlumbachl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Bachillerato Lerdo"		 
		return context


class ListaSinEdadl(LoginRequiredMixin,GroupRequiredMixin,ListView): # Sin Edad lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['lerdo','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaSinEdadl,self).get_queryset().filter(escolaridad='No Tiene Edad escolar',hospital=2,ciclo__status=True).order_by('folio')
		else:
			return super(ListaSinEdadl,self).get_queryset().filter(user=self.request.user,escolaridad='No Tiene Edad escolar',hospital=2,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs):  
		context = super(ListaSinEdadl, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions No Tiene Edad escolar Lerdo"		 
		return context

#Piscicologia

class ListaAlumPishoy(LoginRequiredMixin,GroupRequiredMixin,ListView): # Discapacidad acumulado Gomez
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']
	 
	def get_queryset(self):	
		today = date.today()
		if self.request.user.is_superuser:
			return super(ListaAlumPishoy,self).get_queryset().filter(atencion='Psicologia',fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,ciclo__status=True).order_by('folio')
		else:
			return super(ListaAlumPishoy,self).get_queryset().filter(user=self.request.user,atencion='Psicologia',fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAlumPishoy, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Con Atencion psicología" 
		return context


class ListaAtencionsDiscap(LoginRequiredMixin,GroupRequiredMixin,ListView): # Discapacidad acumulado pisco
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']
	 

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsDiscap,self).get_queryset().filter(atencion='Psicologia',ciclo__status=True).exclude(discapacidad='No').order_by('folio')
		else:
			return super(ListaAtencionsDiscap,self).get_queryset().filter(user=self.request.user,atencion='Psicologia',ciclo__status=True).exclude(discapacidad='No').order_by('folio')

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsDiscap, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions con Discapacidad, atendido por psicología" 
		return context

class ListaAtencionsPrimap(LoginRequiredMixin,GroupRequiredMixin,ListView): # Primaria Psicologia Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsPrimap,self).get_queryset().filter(escolaridad='Primaria',atencion='Psicologia',ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionsPrimap,self).get_queryset().filter(user=self.request.user,escolaridad='Primaria',atencion='Psicologia',ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsPrimap, self).get_context_data(**kwargs)	 
		context['hospital'] = "Concentrado de Atencions Primaria, atendido por psicología"	
		return context

class ListaAtencionsPreep(LoginRequiredMixin,GroupRequiredMixin,ListView): # Prescolar Psicologia Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']
	 
	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsPreep,self).get_queryset().filter(escolaridad='Preescolar',atencion='Psicologia',ciclo__status=True).order_by('folio') 
		else:
			return super(ListaAtencionsPreep,self).get_queryset().filter(user=self.request.user,escolaridad='Preescolar',atencion='Psicologia',ciclo__status=True).order_by('folio') 

	def get_context_data(self, **kwargs): #para saber si  ya  existe el alumo para la foto
		context = super(ListaAtencionsPreep, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Preescolar, atendido por psicología"		 
		return context

class ListaAtencionsSecp(LoginRequiredMixin,GroupRequiredMixin,ListView): # Secundaria lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']	 

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionsSecp,self).get_queryset().filter(escolaridad='Secundaria',atencion='Psicologia',ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionsSecp,self).get_queryset().filter(user=self.request.user,escolaridad='Secundaria',atencion='Psicologia',ciclo__status=True).order_by('folio')

	def get_context_data(self, **kwargs):  
		context = super(ListaAtencionsSecp, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Secundaria, atendido por psicología"		 
		return context

class ListaAtencionestytiedadp(LoginRequiredMixin,GroupRequiredMixin,ListView): # No estudia y tiene edad escalar lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAtencionestytiedadp,self).get_queryset().filter(escolaridad='No Estudia y tiene edad escolar',atencion='Psicologia',ciclo__status=True).order_by('folio')
		else:
			return super(ListaAtencionestytiedadp,self).get_queryset().filter(user=self.request.user,escolaridad='No Estudia y tiene edad escolar',atencion='Psicologia',ciclo__status=True).order_by('folio')			

	def get_context_data(self, **kwargs):  
		context = super(ListaAtencionestytiedadp, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions que No estudia y tiene edad escalar, atendido por psicología"		 
		return context


class ListaAlumbachp(LoginRequiredMixin,GroupRequiredMixin,ListView): # Bachillerato lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']

	def get_queryset(self):	
		if self.request.user.is_superuser:
			return super(ListaAlumbachp,self).get_queryset().filter(escolaridad='Bachillerato',atencion='Psicologia',ciclo__status=True).order_by('folio')
		else:
			return super(ListaAlumbachp,self).get_queryset().filter(user=self.request.user,escolaridad='Bachillerato',atencion='Psicologia',ciclo__status=True).order_by('folio')
	
	def get_context_data(self, **kwargs):  
		context = super(ListaAlumbachp, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions Bachillerato, atendido por psicología"		 
		return context

class ListaSinEdadp(LoginRequiredMixin,GroupRequiredMixin,ListView): # Sin Edad lerdo Acumulado
	context_object_name = 'Atencions'
	template_name = 'principal/Atencionsxx.html'
	model = Atencion
	group_required = ['pisi','super']

	def get_queryset(self):
		if self.request.user.is_superuser:	
			return super(ListaSinEdadp,self).get_queryset().filter(escolaridad='No Tiene Edad escolar',atencion='Psicologia',ciclo__status=True).order_by('folio') 
		else:
			return super(ListaSinEdadp,self).get_queryset().filter(user=self.request.user,escolaridad='No Tiene Edad escolar',atencion='Psicologia',ciclo__status=True).order_by('folio') 			
			
	def get_context_data(self, **kwargs):  
		context = super(ListaSinEdadp, self).get_context_data(**kwargs)		 
		context['hospital'] = "Concentrado de Atencions No Tiene Edad escolar, atendido por psicología"		 
		return context

 

class UpdateAtencion(UpdateView):
	template_name = 'principal/addAtencion.html'
	model = Atencion
	form_class = AddAtencionForm
	success_url = reverse_lazy('principal_app:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateAtencion, self).form_valid(form)
 


class SerchAtencionView(LoginRequiredMixin,GroupRequiredMixin,ListView):
	model = Atencion
	template_name = 'principal/buscaAtencion.html' 
	group_required = ['super']
	

	def get_queryset(self):
		search_query = self.request.GET.get('q',None)
		if search_query:
			queryset = super(SerchAtencionView, self).get_queryset().all()  
		else:
			queryset = ""
			
		q = self.request.GET.get('q', '') 
		#print "sesta es el valor de :" +q
				
		if q:
		    queryset = queryset.filter(
		        Q(folio__icontains=q)|
		        Q(nombre__icontains=q) 
		    )		
		return queryset


class ListDuplicados(ListView):
	context_object_name = 'Atencions'
	template_name = 'principal/duplicados.html'
	model = Atencion

#context['disc_l'] = Atencion.objects.filter(hospital=2,ciclo__status=True).exclude(discapacidad='No').count()

	def get_queryset(self):
		return super(ListDuplicados,self).get_queryset().filter(ciclo__status=True).exclude(
	escolaridad__icontains='No Tiene Edad escolar').filter(ciclo__status=True).exclude(escolaridad__icontains = 'No Estudia y tiene edad escolar'
	).values('hospital__nombre',
	'nombre').annotate(total=Count('nombre')).order_by('nombre')#.filter(total__gt=1) 
	
	def get_context_data(self, **kwargs):
		context = super(ListDuplicados,self).get_context_data(**kwargs)
		context['dobles'] = Atencion.objects.all().values('nombre').annotate(total=Count('nombre')).order_by('nombre') #.filter(total__gt=1) 
		#print context['dobles']
		return context


def listAlxx(request):
    data = serializers.serialize('json', Atencion.objects.filter(ciclo__status=True).order_by('nombre', 'id').distinct(
    'nombre'),fields=('nombre','sexo','coloniaal','callenumal','localidadal',
    'discapacidad','escolaridad','escuela','coloniaesc','direccionesc','localidadesc'))
    out = open('Atencion.json','w')
    out.write(data)
    out.close()
    return HttpResponse(data)

''' 
#from django.core import serializers
#data = serializers.serialize('xml', SomeModel.objects.all(), fields=('name','size'))
''' 

def CargaAtencions(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="atenciones.csv"'
 
    registrants= Atencion.objects.filter(ciclo__status=True).order_by('nombre', 'id').distinct(
    	'nombre')

    writer = csv.writer(response,delimiter="|")
    writer.writerow(['nombre','sexo','coloniaal','callenumal','localidadal',
    'discapacidad','escolaridad','escuela','coloniaesc','direccionesc','localidadesc'])

    for registrant in registrants:
        writer.writerow([registrant.nombre.encode('utf-8'), 
                            registrant.sexo.encode('utf-8'), 
                            registrant.coloniaal.encode('utf-8'),
                            registrant.callenumal.encode('utf-8'),
                            registrant.localidadal.encode('utf-8'),
                            registrant.discapacidad.encode('utf-8'),
                            registrant.escolaridad.encode('utf-8'),
                            registrant.escuela.encode('utf-8'),
                            registrant.coloniaesc.encode('utf-8'),
                            registrant.direccionesc.encode('utf-8'),
                            registrant.localidadesc.encode('utf-8')])

    return response

def ExportaAtenciones(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="atenciones.csv"'
 
    #registrants = Atencion.objects.raw("Select * from principal_atencion a join users_user b ON  a.user_id = b.id  join principal_cicloescolar c ON c.id = a.ciclo_id join principal_Alumno d on d.id = a.alumno_id join principal_hospital e on e.id = a.hospital_id")

    registrants = Atencion.objects.raw("Select * from principal_atencion a \
    	join users_user b ON  a.user_id = b.id  \
		join principal_cicloescolar c ON c.id = a.ciclo_id  \
		join principal_Alumno d on d.id = a.alumno_id \
		join principal_hospital e on e.id = a.hospital_id \
		order by a.id") 
 
    writer = csv.writer(response,delimiter="|")
    writer.writerow(['id','hospital','alumno','ciclo','atencion',
    'modalidad','edad','meses','grado','especialidad','diagnostico','fechaatencion',
    'horainicio','horafin','tema','observacion','sexo','coloniaal',
    'callenumal','localidadal', 'discapacidad','escolaridad','escuela',
    'coloniaesc','direccionesc','localidadesc','user'])
         
    
    for registrant in registrants:
        writer.writerow([registrant.id, 
                            registrant.hospital, 
                            registrant.alumno,
                            registrant.ciclo,
                            registrant.atencion.encode('utf-8'),
                            registrant.modalidad.encode('utf-8'),
                            registrant.edad,
                            registrant.meses,
                            registrant.grado,
                            registrant.especialidad.encode('utf-8'),
                            registrant.diagnostico.encode('utf-8'),
                            registrant.fechaatencion,
                            registrant.horainicio,
                            registrant.horafin,
                            registrant.tema.encode('utf-8'),
                            registrant.observacion.encode('utf-8'),
                            registrant.sexo,
                            registrant.coloniaal.encode('utf-8'),
                            registrant.callenumal.encode('utf-8'),
                            registrant.localidadal.encode('utf-8'),
                            registrant.discapacidad.encode('utf-8'),
                            registrant.escolaridad.encode('utf-8'),
                            registrant.escuela.encode('utf-8'),
                            registrant.coloniaesc.encode('utf-8'),
                            registrant.direccionesc.encode('utf-8'),
                            registrant.localidadesc.strip(),
                            registrant.user])

    return response
 
def CargaAtenciones_ant(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="atenciones.csv"'
 
    registrants= Atencion.objects.all().order_by('folio')

    writer = csv.writer(response,delimiter="|")
    writer.writerow(['id','hospital','atencion','ciclo','modalidad',
    'nombre','edad','meses','grado','especialidad','diagnostico',
    'fechaatencion','horainicio','horafin','tema','observacion','user'])

    for registrant in registrants:
        writer.writerow([registrant.id, 
                            registrant.hospital, 
                            registrant.atencion.encode('utf-8'),
                            registrant.ciclo,
                            registrant.modalidad.encode('utf-8'),
                            registrant.nombre.encode('utf-8'),
                            registrant.edad,
                            registrant.meses,
                            registrant.grado,
                            registrant.especialidad.encode('utf-8'),
                            registrant.diagnostico.encode('utf-8'),
                            registrant.fechaatencion,
                            registrant.horainicio,
                            registrant.horafin,
                            registrant.tema.encode('utf-8'),
                            registrant.observacion.encode('utf-8'),
                            registrant.user])

    return response
 



class AddAtencionViews(LoginRequiredMixin,FormView):
	form_class = AddAtencionForm
	template_name = 'principal/addAtencion.html'
	model = Atencion	
	success_url = '/'
 	
	def get_form(self, form_class):		
		form = super(AddAtencionViews, self).get_form(form_class)
		form.fields['hospital'].queryset = Hospital.objects.filter(usuarios__pk= self.request.user.id)
		return form	
    
	def form_valid(self, form, *args, **kwargs): 
 		#xfolio =  Atencion.objects.count()+1

 		xciclo = Cicloescolar.objects.get(status=True)
 		form.instance.ciclo = xciclo 
		form.instance.user = self.request.user	 
		form.alumno = self.required.POST['id_alumno']
		#self.kwargs['id']
		print 'va formulario'
		form.save()
 		return super(AddAtencionViews, self).form_valid(form)

 	def form_invalid(self,form):
 		print 'no'	
 		return super(AddAtencionViews,self).form_invalid(form)



class AddAlumno(LoginRequiredMixin,FormView):
	model = Alumno
	form_class = AlumnoForm
	template_name = 'principal/addAlumno.html'
	success_url = '/listalumnos'

	
	def form_valid(self, form ): 
		form.instance.user = self.request.user
		form.escuela  = self.request.POST['escuela']
		form.save()
		return super(AddAlumno, self).form_valid(form)

	def form_invalid(self,form):	
		print self.request.POST['escuela']
		print 'no'	 	 
		return super(AddAlumno, self).form_invalid(form) 



class ListAlumnos(LoginRequiredMixin,ListView):
	context_object_name = 'alu'
	template_name = 'principal/alumno_list.html'
	model = Alumno

	def get_queryset(self):
		search_query = self.request.GET.get('q',None)
		if search_query:
			print 'si'
			queryset = super(ListAlumnos, self).get_queryset().all()   
		else:
			print 'no'
			queryset = super(ListAlumnos, self).get_queryset().all().order_by('-fecha')[:4] 
			
		q = self.request.GET.get('q', '') 
		print "sesta es el valor de :" +q
				
		if q:
		    queryset = queryset.filter(
		        Q(id__icontains=q)|
		        Q(nombre__icontains=q) 
		    )		
		return queryset
 
	def get_context_data(self, **kwargs):
		context = super(ListAlumnos,self).get_context_data(**kwargs)
		context['aluxx'] = Alumno.objects.all().order_by('-fecha')[:4]
	 
		return context

def persona_auto_complete(request):
	q = request.GET.get('term','')	
	print q
 	if q:
  		qset = (
   		Q(nombre__icontains=q)    		
   	)
  		personas = Alumno.objects.filter(qset).distinct()  		
  		personas_list = []  		 
 	else:
  		personas = []
 		personas_list = []

 	for p in personas:
  		value = '%s, (%s)' % (p.nombre,p.callenum)
  		p_dict = {'id': p.id, 'label': value, 'value': value}
  		personas_list.append(p_dict)
 	return HttpResponse(simplejson.dumps(personas_list))

def escuela_auto_completa(request):
	q = request.GET.get('term','')
	if q:
		qset = (
			Q(nombre__icontains=q)
	)
		escuelas = Escuela.objects.filter(qset).distinct()
		escuelas_list = []
	else:
		escuelas = []
		escuelas_list=[]

	for p in escuelas:
		value = '%s, (%s , %s, %s)' % (p.nombre, p.colonia, p.localidad, p.turno)
		e_dict = {'id': p.id, 'label' : value, 'value': value, 'value': value,'value': value}
		escuelas_list.append(e_dict)
	return HttpResponse(simplejson.dumps(escuelas_list))


def ListaAlumnos1_ajax(request):
	if request.is_ajax():
		palabra = request.GET.get('term','')
		
	
		alum = Alumno.objects.filter(nombre__icontains =palabra)
			
		results=[]
		
		for a in alum:
			alum_json={}
			alum_json['label'] = a.nombre
			alum_json['value'] = a.nombre
			results.append(alum_json)

		data_json = json.dumps(results)
		print data_json

	else:
		 data_json='fail'
	mimetype="application/json"
	return HttpResponse(data_json,mimetype)

def ListaAlumnos99_ajax(request):
	if request.is_ajax():
		palabra = request.GET.get('q','')
		
	
		alum = Alumno.objects.filter(nombre__icontains =palabra)
			
		results=[]		
		for a in alum:
			alum_json={}
			alum_json['label'] = a.nombre
			alum_json['value'] = a.nombre
			results.append(alum_json)			 

		data_json = json.dumps(results)
		print data_json
		
	else:
		 data_json='fail'
	mimetype="application/json"
	return HttpResponse(data_json,mimetype)

def ListaAlumnos_ajax(request):
	if request.is_ajax():
		palabra = request.GET.get('q','')
		alum = Alumno.objects.filter(nombre__icontains=palabra)
		results=[]
		for a in alum:
			alum_json={}
			alum_json['id'] = a.id
			alum_json['nombre'] = a.nombre
			results.append(alum_json)

		data_json = json.dumps(results)
		print data_json
	else:
		data_json='fail'
	mimetype="application/json"
	return HttpResponse(data_json,mimetype)

def ListaAlumnosxxx_ajax(request): # JsonResponse 1.7 Carga  un combo
	if request.is_ajax():
		gdo = Alumno.objects.filter(nombre__icontains = request.GET['q'])	
		data = serializers.serialize("json",gdo)
		return JsonResponse(data, safe=False)
	else:
		raise Http404

def SubeAlumnos(request):  
    f = open('meme.csv', 'r')  
    for line in f:
        line =  line.split(',')
        Ald = Alumno() 
        if line[0] != 'nombre':
	        Ald.nombre       = line[0]
	        Ald.sexo         = line[1]
	        Ald.colonia      = line[2]
	        Ald.callenum   = line[3]
	        Ald.localidadal  = line[4]
	        Ald.discapacidad = line[5]
	        Ald.escolaridad  = line[6]
	        Ald.escuela      = line[7]
	        Ald.coloniaesc   = line[8]
	        Ald.direccionesc = line[9]
	        Ald.localidadesc = line[10]  
	        Ald.save()
    f.close()
    return HttpResponse()

def subeAtenciones(request):
	f = open('atenciones.csv','r')
	for li in f:
		li = li.split(',')
		at = Atencion.objects.create()
		if li[0] != 'id':
			at.folio         = li[0]
			at.hospital      = li[1]
			at.atencion      = li[2]
			#at.ciclo         = li[3]
			at.modalidad     = li[4]
			at.nombre        = li[5]
			at.edad          = li[6]
			at.meses         = li[7]
			at.grado         = li[8]
			at.especialidad  = li[9]
			at.diagnostico   = li[10]
			at.fechaatencion = li[11]
			at.horainicio    = li[12]
			at.horafin       = li[13]
			at.tema          = li[14]
			at.observacion   = li[15]
			at.profa         = li[16]
			at.save()
	f.close()
	return HttpResponse()



def update_pk_alumno(request):
	f = csv.reader(open('atenciones.csv','w'),delimiter='|')
	for li in f:	
		if li[0] != 'id':
			nom  = li[5]			 
			#print nom
			al= Alumno.objects.raw("select id from principal_Alumno where nombre = %s",[nom])			 
			for a in al:				
				li.insert(0,'PK')
				li.append(a.id)
				print a.id,nom
	return HttpResponse()


def addalumodel(request):
	if request.method == 'POST':
		
		nombre 	      = request.POST.get('nombre',None)
		sexo          = request.POST.get('sexo')
		colonia       = request.POST.get('colonia', None)
		calle         = request.POST.get('calle',None)
		localidad     = request.POST.get('localidad',None)
		discapacidad  = request.POST.get('discapacidad')
		escolaridad   = request.POST.get('escolaridad')
		 
		 
		Alumno.objects.create(nombre = nombre,
							sexo = sexo,
							colonia = colonia,
							callenum = calle,
							localidad = localidad,
							discapacidad = discapacidad,
							escolaridad = escolaridad)

		return HttpResponse("/")

def edad_alumno_ajax(request):
        if request.is_ajax():
                alumno = Alumno.objects.get(id = request.GET['id'])

                response = JsonResponse({'edad': alumno.edad(), 'mes':alumno.mes()})
                return HttpResponse(response.content)
        else:
              
        	return HttpResponse('/')
	
