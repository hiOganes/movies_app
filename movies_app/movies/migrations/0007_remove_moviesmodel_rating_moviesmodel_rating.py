# Generated by Django 5.1.2 on 2024-10-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_moviesmodel_rating_moviesmodel_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesmodel',
            name='rating',
        ),
        migrations.AddField(
            model_name='moviesmodel',
            name='rating',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
