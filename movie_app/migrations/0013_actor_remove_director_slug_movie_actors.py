# Generated by Django 5.0.6 on 2024-07-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_alter_director_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='director',
            name='slug',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie_app.actor'),
        ),
    ]
