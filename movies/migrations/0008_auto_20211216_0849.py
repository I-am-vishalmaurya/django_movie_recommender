# Generated by Django 2.2.5 on 2021-12-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_original_movies_table_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='original_movies_table',
            old_name='language',
            new_name='original_language',
        ),
        migrations.RenameField(
            model_name='original_movies_table',
            old_name='title',
            new_name='original_title',
        ),
        migrations.RemoveField(
            model_name='original_movies_table',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='original_movies_table',
            name='ratings',
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='adult',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='genres',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='imdb_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='runtime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='spoken_languages',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='status',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='original_movies_table',
            name='tmdb_id',
            field=models.IntegerField(null=True),
        ),
    ]
