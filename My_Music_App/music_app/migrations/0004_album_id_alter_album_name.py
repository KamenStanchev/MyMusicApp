# Generated by Django 4.0.5 on 2022-06-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_alter_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Album Name'),
        ),
    ]