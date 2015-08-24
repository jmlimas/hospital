from django.db import models 
from django.conf import settings
 


class TimeStampModel(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
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
    
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["pk"]


# Create your models here.
class Alumno(TimeStampModel):
    
    Opsexo = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        )

    Op2 = (
        ('Si', 'Si'),
        ('No', 'No')
        )

    opesc=(
        ('Preescolar','Preescolar'),
        ('Primaria' ,'Primaria'),
        ('Secundaria','Secundaria'),
        ('No Estudia y tiene edad escolar',  'No Estudia y tiene edad escolar'),      
        ('Bachillerato', 'Bachillerato'),
        ('No Tiene Edad escolar',  'No Tiene Edad escolar'),
        )
    Disca=(
        ('No', 'No'),
        ('Motriz','Motriz'),
        ('Visual', 'Visual'),
        ('Auditiva', 'Auditiva'),
        ('Intelectual', 'Intelectual'),
        ('Otra', 'Otra'),
        )

    tp =(
            ('Pediatria','Pediatria'),
            ('ConsultaExt','Consulta Externa'),
            ('AtencionDom','Atencion Domiciliaria'),
        )

    folio = models.IntegerField()
    hospital = models.ForeignKey('Hospital')   
    ciclo = models.ForeignKey('Cicloescolar',default=1)
    modalidad = models.CharField(max_length=25,null=True,default=True,choices=tp)
    nombre = models.CharField(max_length=180)
    edad = models.IntegerField()
    meses = models.IntegerField()
    sexo = models.CharField(max_length=1,choices=Opsexo)
    coloniaal = models.CharField(max_length=100)
    callenumal = models.CharField(max_length=100)
    localidadal = models.CharField(max_length=80)
    discapacidad = models.CharField(max_length=12,choices=Disca)
    grado = models.IntegerField()
    escolaridad = models.CharField(max_length=40,choices=opesc)
    escuela = models.CharField(max_length=100)
    coloniaesc = models.CharField(max_length=80)
    direccionesc = models.CharField(max_length=120, null=True,blank=True)
    localidadesc = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=80)
    diagnostico = models.CharField(max_length=80)
    fechaatencion  = models.DateField()
    horainicio = models.TimeField()
    horafin = models.TimeField()   
    tema = models.CharField(max_length=80)
    observacion = models.TextField()
    

    def __unicode__(self):
        return self.nombre   

 

class Escuela(TimeStampModel):
	nombre = models.CharField(max_length=180)
	direccion = models.CharField(max_length=180)

	def __unicode__(self):
		return self.nombre




