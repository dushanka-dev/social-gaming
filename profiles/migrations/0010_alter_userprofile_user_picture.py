# Generated by Django 3.2 on 2022-02-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_userprofile_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_picture',
            field=models.ImageField(default='media/uploads/default-image.png', upload_to='uploads/'),
        ),
    ]
