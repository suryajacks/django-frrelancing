# Generated by Django 4.2 on 2023-07-23 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0002_student1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student1',
            name='Mobile_number1',
            field=models.IntegerField(blank=True),
        ),
    ]
