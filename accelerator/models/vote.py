from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Vote(models.Model):
    interestingly = models.BooleanField(
        verbose_name='Интересно',
    )
    voter = models.ForeignKey(
        'users.Profile',
        on_delete=models.SET_NULL,
        null=True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
