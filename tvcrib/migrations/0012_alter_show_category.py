# Generated by Django 3.2.4 on 2021-07-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrib', '0011_auto_20210703_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='category',
            field=models.ManyToManyField(related_name='shows', to='tvcrib.Category'),
        ),
    ]
