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

class Move(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(null=True, blank=True)
    pp = models.SmallIntegerField(null=True, blank=True)
    accuracy = models.SmallIntegerField(null=True, blank=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(null=True, blank=True)
    contest_type_id = models.IntegerField(null=True, blank=True)
    contest_effect_id = models.IntegerField(null=True, blank=True)
    super_contest_effect_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'moves'

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(null=True, blank=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    class Meta:
        db_table = 'pokemon'
