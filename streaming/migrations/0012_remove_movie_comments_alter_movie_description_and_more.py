# Generated by Django 4.2.6 on 2023-10-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0011_rename_cover_img_movie_cover_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comments',
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='premiere_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
