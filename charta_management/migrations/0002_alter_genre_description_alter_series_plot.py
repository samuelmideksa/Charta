# Generated by Django 5.0.2 on 2024-03-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charta_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='plot',
            field=models.TextField(blank=True, null=True),
        ),
    ]