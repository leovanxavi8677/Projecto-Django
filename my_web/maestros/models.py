from ..personas.models import Persona
from django.db import models
#from ..areamaestro.models import AreaExpertise

ESTATUS_CHOICES = [
    ('A','Activo'),
    ('ST','Suspendido'),
    ('P','Permiso'),
    ('SD','Suspendido Definitivo')
]

class Maestro(Persona):
    cubiculo = models.CharField(max_length=50, blank=False, null=False)
    numeroTrabajdor = models.CharField(max_length=13, blank=False, null=False)
    estatus = models.CharField(max_length=2, blank=False, null=False)
    #areaExpertise = models.ManyToManyField(AreaExpertise,help_text="Seleccione un Área",related_name="maestroAreaExpertise",on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {}".format(self.cubiculo, self.numeroTrabajdor,self.estatus)
