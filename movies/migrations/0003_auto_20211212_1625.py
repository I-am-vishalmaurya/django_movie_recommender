# Generated by Django 2.2.5 on 2021-12-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211212_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_collected',
            name='imdb_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='movie_collected',
            name='tmdb_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
