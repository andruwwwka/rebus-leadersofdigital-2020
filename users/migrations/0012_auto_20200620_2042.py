# Generated by Django 3.0.7 on 2020-06-20 20:42
from django.db import migrations


def create_departments(apps, schema_editor):
    """Создание подразделений."""
    departments = [
        {
            'name': 'Департамент комплексных проектов',
        },
        {
            'name': 'Департамент финансов',
        }
    ]

    Department = apps.get_model('organization', 'Department')
    for departments_data in departments:
        Department.objects.create(**departments_data)


def create_positions(apps, schema_editor):
    """Создание должности."""
    Position = apps.get_model('users', 'Position')
    Position.objects.create(
        post="Специалист"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200620_1143'),
    ]

    operations = [
        migrations.RunPython(create_departments),
        migrations.RunPython(create_positions),
    ]
