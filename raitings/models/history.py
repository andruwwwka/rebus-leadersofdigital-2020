from django.db import models


class History(models.Model):
    amount = models.IntegerField()
    badge = models.ForeignKey()
    reward = models.ForeignKey()
    profile = models.ForeignKey()
