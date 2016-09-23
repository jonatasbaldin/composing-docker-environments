from django.db import models


class AwesomeCounter(models.Model):
    name = models.CharField(max_length=255)
    counter = models.IntegerField(null=True, default=0)
