# Generated by Django 4.2 on 2023-07-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0006_delete_question1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer1', models.TextField(verbose_name=50)),
                ('Answer2', models.TextField(verbose_name=50)),
                ('Answer3', models.TextField(verbose_name=50)),
            ],
        ),
    ]
