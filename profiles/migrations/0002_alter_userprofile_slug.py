# Generated by Django 3.2 on 2022-02-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
