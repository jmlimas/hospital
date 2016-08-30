# -*- coding: utf-8 -*-
from django.db import models 
from django.conf import settings

from datetime import date,datetime
import datetime 




class TimeStampModel(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,null=True,blank=True)
    fecha    = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True


class Cicloescolar(TimeStampModel):
    descripcion = models.CharField(max_length=80)
    fechaini = models.DateField()
    fechafin = models.DateField()
    status = models.BooleanField(default=True) 

    def __unicode__(self):
        return self.descripcion


class Hospital(TimeStampModel):
    nombre = models.CharField(max_length=60)
    usuarios = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name= 'hospital_user')
       
    def __unicode__(self):
        return self.nombre

    def get_usuarios(self):
        return "\n".join([u.username for u in self.usuarios.all()])

    class Meta:
        ordering = ["pk"]


class Escuela(TimeStampModel):
    OPturno = (
        ('TV', 'Turno Vespertino'),
        ('TM', 'Turno Matutino'),
        )

    nombre = models.CharField(max_length=180)
    colonia = models.CharField(max_length=180)
    direccion = models.CharField(max_length=120, null=True, blank=True)
    localidad = models.CharField(max_length=100)
    turno = models.CharField(max_length=2, null=True, blank=True,choices=OPturno)

    def __unicode__(self):
        return self.nombre

    def seave(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.lower()
        super(Escuela, self).save(force_insert, force_update)


 
class Alumno(models.Model):
  
    nombre = models.CharField(max_length=180,db_index=True) #   
    sexo = models.CharField(max_length=1, null=True, blank=True) #
    colonia = models.CharField(max_length=100,null=True, blank=True) #
    callenum = models.CharField(max_length=100,null=True, blank=True) #
    localidad = models.CharField(max_length=80,null=True, blank=True) #
    discapacidad = models.CharField(max_length=12,null=True, blank=True) #
    escolaridad = models.CharField(max_length=40,null=True, blank=True) #
    fechanaciomiento = models.DateField()
  
     
    def __unicode__(self):
        return self.nombre
 
    def edad(self):
        import datetime
        today = datetime.date.today()
        #return  ((today.year - self.fechanaciomiento.year-1)+(1 if(today.month, today.day)>=(self.fechanaciomiento.month, self.fechanaciomiento.day) else 0))
        return today.year - self.fechanaciomiento.year + (today.month-self.fechanaciomiento.month)/12

    def mes(self):
        import datetime
        today = datetime.date.today()
        #today = datetime.date(2016, 10, 6)  # aqui  pongo a  fecha que se me da la gana no solo la  de  hoy
        #return today.year - self.fechanaciomiento.year + (today.month-self.fechanaciomiento.month)/12,  (today.month-self.fechanaciomiento.month)%12 # año y mes
        return (today.month-self.fechanaciomiento.month)%12  # solo Mes
 
 


    #def save(self, force_insert=False, force_update=False):
    #    self.nombre = self.nombre.lower()
    #    super(Alumno, self).save(force_insert, force_update)

    #def clean(self):
    #    if self.nombre:
    #        self.nombre = self.nombre.strip()



 
class Atencion(TimeStampModel):
      
    tp =(
            ('Pediatria','Pediatria'),
            ('ConsultaExt','Consulta Externa'),
            ('AtencionDom','Atencion Domiciliaria'),
        )
    
    at = (
            ('Pedagogia','Pedagogia'),
            ('Psicologia','Psicologia'),
        )

    hospital = models.ForeignKey('Hospital')  
    alumno = models.ForeignKey('Alumno') 
    ciclo = models.ForeignKey('Cicloescolar')
    atencion = models.CharField(max_length=10,null=True,blank=True,choices=at)     
    modalidad = models.CharField(max_length=25,null=True,default=True,choices=tp)
    edad = models.IntegerField(default=0) #
    meses = models.IntegerField(default=0) #
    grado = models.IntegerField(default=0) 
    especialidad = models.CharField(max_length=80)
    diagnostico = models.CharField(max_length=80)
    fechaatencion  = models.DateField()
    horainicio = models.TimeField(default=datetime.datetime.utcnow,null=True,blank=True)
    horafin = models.TimeField(default=datetime.datetime.utcnow,null=True,blank=True)   
    tema = models.CharField(max_length=80,default="xxx", null=True,blank=True)
    observacion = models.TextField(default="xxx",null=True,blank=True)
    
    
    def __unicode__(self):
        return self.alumno.nombre   

    