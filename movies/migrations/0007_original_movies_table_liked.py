# Generated by Django 2.2.5 on 2021-12-16 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movie_details_original_movies_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='original_movies_table',
            name='liked',
            field=models.BigIntegerField(null=True),
        ),
    ]
