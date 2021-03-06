# Generated by Django 3.0.7 on 2020-06-21 03:38

import random
from django.db import migrations


def create_votes_for_tenders(apps, schema_editor):
    """Создание тестовых лайков и дизлайков к тендерам."""
    Tender = apps.get_model('accelerator', 'Tender')
    Profile = apps.get_model('users', 'Profile')
    Vote = apps.get_model('accelerator', 'Vote')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    for _ in range(25):
        profile = Profile.objects.all().order_by('?').first()
        tender = Tender.objects.all().order_by('?').first()
        tender_type = ContentType.objects.get_for_model(tender)
        vote_already_exists = Vote.objects.filter(
            voter=profile,
            content_type__pk=tender_type.id,
            object_id=tender.id
        ).exists()
        if not vote_already_exists:
            Vote.objects.create(
                voter=profile,
                content_type=tender_type,
                object_id=tender.id,
                interestingly=bool(random.getrandbits(1))
            )


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0008_auto_20200621_0221'),
    ]

    operations = [
        migrations.RunPython(create_votes_for_tenders),
    ]
