#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pointing(models.Model):
    no_grilles = models.FloatField()
    
    def __str__(self):
        return "Combien de grilles ? = {}".format(self.no_grilles)
