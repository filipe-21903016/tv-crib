# Generated by Django 3.2.4 on 2021-07-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrib', '0008_auto_20210703_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='cardCover',
            field=models.ImageField(blank=True, null=True, upload_to='./fd1ab63aece5497287e69101a6833a1d'),
        ),
        migrations.AlterField(
            model_name='show',
            name='movieCover',
            field=models.ImageField(blank=True, null=True, upload_to='./6dd057106b2c4725b755d4c30e1127a9'),
        ),
    ]
