# Generated by Django 4.2.6 on 2023-10-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0002_actor_created_at_alter_comment_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='type',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Show', 'Show')], default='Show', max_length=6),
        ),
    ]
