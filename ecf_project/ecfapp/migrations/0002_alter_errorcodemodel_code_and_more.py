# Generated by Django 4.2.10 on 2024-03-18 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecfapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorcodemodel',
            name='code',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='errorcodemodel',
            name='meaning',
            field=models.CharField(max_length=300),
        ),
    ]
