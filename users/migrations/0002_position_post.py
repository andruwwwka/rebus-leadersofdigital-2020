# Generated by Django 3.0.7 on 2020-06-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='post',
            field=models.CharField(choices=[('head', 'Руководитель'), ('alternative_head', 'Заместитель руководителя'), ('senior', 'Ведущий эксперт'), ('middle', 'Эксперт'), ('junior', 'Младший эксперт')], default='junior', max_length=128),
        ),
    ]
