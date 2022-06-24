# Generated by Django 4.0.5 on 2022-06-23 18:27

import My_Music_App.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), My_Music_App.validators.username_validator], verbose_name='Username'),
        ),
    ]
