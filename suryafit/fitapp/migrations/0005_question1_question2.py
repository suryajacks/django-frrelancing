# Generated by Django 4.2 on 2023-07-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0004_alter_student1_mobile_number1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.TextField(verbose_name=50)),
                ('Answer1', models.TextField(verbose_name=50)),
                ('Answer2', models.TextField(verbose_name=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer1', models.TextField(verbose_name=50)),
                ('Answer2', models.TextField(verbose_name=50)),
                ('Answer3', models.TextField(verbose_name=50)),
            ],
        ),
    ]
