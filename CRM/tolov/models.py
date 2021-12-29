from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from shartnomaApp.models import *

class Tolov(models.Model):
    years = ( 
    ("2022", "2022"), 
    ("2023", "2023"), 
    ("2024", "2024"), 
    ("2025", "2025"),
    ) 

    months = ( 
    ("January", "January"), 
    ("February", "February"), 
    ("March", "March"), 
    ("April", "April"), 
    ("May", "May"), 
    ("June", "June"), 
    ("Jule", "Jule"), 
    ("August", "August"), 
    ("September", "September"), 
    ("October", "October"), 
    ("November", "November"), 
    ("December", "December"),  
    )
    shartnoma = models.ForeignKey(Shartnoma, on_delete=models.SET_NULL, null=True)
    ustoz = models.ForeignKey(Ustoz, on_delete=SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=SET_NULL, null=True)
    yil = models.IntegerField()
    tolov_oyi = models.CharField(max_length=20)
    chegirma_status = models.CharField(max_length=10, choices=years)
    ch_sababi = models.CharField(max_length=50)
    ch_miqdori = models.PositiveBigIntegerField()
    t_sanasi = models.DateField()
    kassir = models.CharField(max_length=30)
    tolashi_lozim = models.PositiveBigIntegerField()
    naqd = models.PositiveBigIntegerField()
    bank = models.PositiveBigIntegerField()
    plastik = models.PositiveBigIntegerField()
    click = models.PositiveBigIntegerField()
    jami_tolandi = models.PositiveBigIntegerField()
    jami_qoldi = models.PositiveBigIntegerField()
    def __str__(self):
        return(self.shartnoma)