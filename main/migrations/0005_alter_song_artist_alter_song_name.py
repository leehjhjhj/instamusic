# Generated by Django 4.2.2 on 2023-06-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_song_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
