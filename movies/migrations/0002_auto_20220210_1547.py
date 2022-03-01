# Generated by Django 2.2.5 on 2022-02-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieratings',
            name='tmdb_id',
        ),
        migrations.AddField(
            model_name='movieratings',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie_Collected'),
        ),
    ]