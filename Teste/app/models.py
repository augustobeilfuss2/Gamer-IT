 

"""
Definition of models.
"""

from django.db import models

class Players(models.Model):

    SETOR_CHOICES = (
        ("TI", "TI"),       
    )


    nmcolaborador = models.CharField(
        max_length= 400,
        null= False,
        blank = False,
        unique=True

        
        )

    imcolaborador = models.CharField(
        max_length= 400,
        null= False,
        blank = False
        
        )

    nmSetor = models.CharField(
        max_length= 400,
        null= False,
        blank = False,
        choices = SETOR_CHOICES
            
        )
   

   

class Cursos(models.Model):

    PLAYERS_CHOICES = Players.objects.values_list('nmcolaborador', 'nmcolaborador')


    nmCurso = models.CharField(
        max_length= 255,
        null= False,
        blank = False,
        
        )

    acFaculdade= models.BooleanField(
        null= False,
        blank = False,
        default= False
        
        )

    nuMaterias = models.IntegerField(
        null= False,
        blank = False,
        default= 0
        
        )

    nmInstituicao = models.CharField(
        max_length= 400,
        null= False,
        blank = False
        
        )

     
    nmPlayer = models.CharField(
        
        max_length= 400,
        null= True,
        blank = False,
        choices= PLAYERS_CHOICES
        
        )

    nuHoras = models.IntegerField(
        null= False,
        blank = False
        
        )

 

    ptHoras = models.FloatField(
        null= True,
        blank = True,
        #decimal_places = 2,
        #max_digits= 4,
        default= 0
        
        )

      
    acWorkshop= models.BooleanField(
        null= False,
        blank = True,
        
        )

    ptWorkshop = models.FloatField(
        null= True,
        blank = True,
        #decimal_places = 2,
        #max_digits= 4,
     
        default= 0
        
        )

    acImplementacao= models.BooleanField(
        null= False,
        blank = False,
        
        )

    ptImplementacao = models.FloatField(
        null= True,
        blank = True,
        #decimal_places = 2,
        #max_digits= 4,
        default= 0
        
        )

    acComunik= models.BooleanField(
        null= False,
        blank = False,
        default= False
        )

    ptComunik = models.FloatField(
        null= True,
        blank = True,
        #decimal_places = 2,
        #max_digits= 4,
        default= 0
        )

   


# Create your models here.
