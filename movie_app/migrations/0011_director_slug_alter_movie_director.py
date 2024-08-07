# Generated by Django 5.0.6 on 2024-07-11 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
        ),
    ]
