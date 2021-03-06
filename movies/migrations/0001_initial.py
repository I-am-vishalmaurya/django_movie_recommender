# Generated by Django 2.2.5 on 2022-02-07 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Collected',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tmdb_id', models.IntegerField(null=True, unique=True)),
                ('original_title', models.CharField(max_length=1000)),
                ('original_language', models.CharField(max_length=1000, null=True)),
                ('overview', models.TextField(null=True)),
                ('genres', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.CharField(max_length=1000, null=True)),
                ('production_company', models.CharField(max_length=1000, null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('revenue', models.BigIntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('adult', models.BooleanField(null=True)),
                ('budget', models.BigIntegerField(null=True)),
                ('spoken_languages', models.TextField(null=True)),
                ('status', models.CharField(max_length=1000, null=True)),
                ('runtime', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(null=True, unique=True)),
                ('cast', models.TextField(null=True)),
                ('crew', models.TextField(null=True)),
                ('director', models.CharField(max_length=1000, null=True)),
                ('soup', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(null=True, unique=True)),
                ('rating', models.IntegerField(null=True)),
                ('review', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
