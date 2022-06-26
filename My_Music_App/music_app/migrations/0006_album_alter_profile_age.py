# Generated by Django 4.0.5 on 2022-06-24 15:52

import My_Music_App.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0005_delete_album_alter_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Album Name')),
                ('artist', models.CharField(max_length=30, verbose_name='Artist')),
                ('genre', models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Country Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30, verbose_name='Genre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[My_Music_App.validators.positive_float_validator], verbose_name='Price')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
    ]