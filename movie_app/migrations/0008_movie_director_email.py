# Generated by Django 5.0.6 on 2024-07-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_movie_director_alter_movie_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='sugar_daddy@gmail.com', max_length=254),
        ),
    ]