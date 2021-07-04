# Generated by Django 3.2.4 on 2021-07-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrib', '0004_merge_20210703_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='cardCover',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(max_length=900),
        ),
        migrations.AlterField(
            model_name='show',
            name='movieCover',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>/'),
        ),
    ]
