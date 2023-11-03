# Generated by Django 4.2.6 on 2023-10-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0004_movie_rating_alter_actor_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='show',
            name='country',
        ),
        migrations.RemoveField(
            model_name='show',
            name='language',
        ),
        migrations.AlterField(
            model_name='show',
            name='quality',
            field=models.CharField(choices=[('CAM', 'CAM'), ('SD', 'SD'), ('HD', 'HD'), ('UHD', 'UHD')], default='HD', max_length=5),
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ManyToManyField(blank=True, to='streaming.country'),
        ),
        migrations.AddField(
            model_name='show',
            name='country',
            field=models.ManyToManyField(blank=True, to='streaming.country'),
        ),
        migrations.AddField(
            model_name='show',
            name='language',
            field=models.ManyToManyField(blank=True, to='streaming.language'),
        ),
    ]