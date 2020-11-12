from django.db import models

# Create your models here.


class Parta(models.Model):
    PartaId = models.AutoField(primary_key=True)
    TotalIncome = models.IntegerField()
    TotalLoss = models.IntegerField()
    Year = models.IntegerField()

class Partb(models.Model):
    PartbId = models.AutoField(primary_key=True)
    TotalExpenditure = models.IntegerField()
    BookingScore = models.IntegerField()
    Year = models.IntegerField()