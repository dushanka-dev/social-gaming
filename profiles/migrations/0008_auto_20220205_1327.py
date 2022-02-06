# Generated by Django 3.2 on 2022-02-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_userprofile_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]