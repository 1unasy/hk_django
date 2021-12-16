from django.db import models

class MusinsaOuter(models.Model):
    item_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    brand = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'musinsa_outer'