# Generated by Django 5.0.7 on 2024-07-25 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_compensation_alter_employee_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='compensation',
            new_name='compensations',
        ),
    ]
