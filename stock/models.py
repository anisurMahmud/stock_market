from django.db import models

# Create your models here.

class stock(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=100)
    high = models.DecimalField(max_digits=4, decimal_places=2)
    low = models.DecimalField(max_digits=4, decimal_places=2)
    open = models.DecimalField(max_digits=4, decimal_places=2)
    close = models.DecimalField(max_digits=4, decimal_places=2)
    volume = models.IntegerField()

