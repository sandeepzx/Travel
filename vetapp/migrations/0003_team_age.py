# Generated by Django 4.1.7 on 2023-05-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetapp', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='age',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]