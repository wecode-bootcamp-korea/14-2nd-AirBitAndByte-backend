from django.db import models


class Country(models.Model):
    name       = models.CharField(max_length=200)
    latitube   = models.DecimalField(max_digits=10, decimal_paces=6)
    longitube  = models.DecimalField(max_digits=10, decimal_paces=6)
    province   = models.ForeignKey('province', on_delete=models.CASCADE)

    class Meta:
        db_table  = 'countries'

class Province(models.Model):
    name       = models.CharField(max_length=200)
    latitube   = models.DecimalField(max_digits=10, decimal_paces=6)
    longitube  = models.DecimalField(max_digits=10, deciaml_paces=6)
    city       = models.ForeignKey('city', on_delete=models.CASCADE)

    class Meta:
        db_table  = 'provinces'

class City(models.Model):
    name       = models.CharField(max_length=200)
    latitube   = models.DecimalField(max_digits=10, decimal_paces=6)
    longitube  = models.DecimalField(max_digits=10, deciaml_paces=6)
    province   = models.ForeignKey('province', on_delete=models.CASCADE)

    class Meta:
        db_table  = 'cities'

class District(models.Model):
    name       = models.CharField(max_length=200)
    latitube   = models.DecimalField(max_digits=10, decimal_paces=6)
    longitube  = models.DecimalField(max_digits=10, deciaml_paces=6)
    district  = models.ForeignKey('district', on_delete=models.CASCADE)

    class Meta:
        db_table  = 'districts'

class Street(models.Model):
    name      = models.CharField(max_length=200)
    latitube   = models.DecimalField(max_digits=10, decimal_paces=6)
    longitube  = models.DecimalField(max_digits=10, deciaml_paces=6)

    class Meta:
        db_table  = 'streets'
