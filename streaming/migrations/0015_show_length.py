# Generated by Django 4.2.6 on 2023-10-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0014_actor_thumbnail_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='length',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
