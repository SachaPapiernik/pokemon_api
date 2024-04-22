from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(null=True)
    fling_effect_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'items'