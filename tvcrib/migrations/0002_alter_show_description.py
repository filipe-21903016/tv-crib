# Generated by Django 3.2.4 on 2021-06-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
