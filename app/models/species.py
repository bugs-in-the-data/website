from __future__ import unicode_literals

from django.db import models

class SpeciesModel(models.Model):
    sample_id = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    drainage = models.CharField(max_length=150)

    def getData(self):
        test = {
            'name': 'Ty'
        }
        return test
