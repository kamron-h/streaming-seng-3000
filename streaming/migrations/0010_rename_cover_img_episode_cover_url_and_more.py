# Generated by Django 4.2.6 on 2023-10-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0009_alter_country_region_alter_genre_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='cover_img',
            new_name='cover_url',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='cover_img',
            new_name='cover_url',
        ),
    ]