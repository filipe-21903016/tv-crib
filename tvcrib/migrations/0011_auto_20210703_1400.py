# Generated by Django 3.2.4 on 2021-07-03 13:00

from django.db import migrations, models
import tvcrib.models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrib', '0010_auto_20210703_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='cardCover',
            field=models.ImageField(blank=True, null=True, upload_to=tvcrib.models.get_card_cover_name),
        ),
        migrations.AlterField(
            model_name='show',
            name='movieCover',
            field=models.ImageField(blank=True, null=True, upload_to=tvcrib.models.get_movie_cover_name),
        ),
    ]
