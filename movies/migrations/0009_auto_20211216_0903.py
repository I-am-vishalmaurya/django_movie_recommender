# Generated by Django 2.2.5 on 2021-12-16 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_movies', '0003_auto_20211216_0903'),
        ('movies', '0008_auto_20211216_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_details',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie_Collected'),
        ),
        migrations.DeleteModel(
            name='Original_Movies_Table',
        ),
    ]
