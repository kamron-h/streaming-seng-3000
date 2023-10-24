# Generated by Django 4.2.6 on 2023-10-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0012_remove_movie_comments_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='country',
        ),
        migrations.AddField(
            model_name='actor',
            name='country',
            field=models.ManyToManyField(blank=True, to='streaming.country'),
        ),
    ]
