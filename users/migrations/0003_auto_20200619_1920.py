# Generated by Django 3.0.7 on 2020-06-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_position_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='post',
            field=models.CharField(max_length=256),
        ),
    ]
