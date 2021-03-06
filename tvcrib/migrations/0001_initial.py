# Generated by Django 3.2.4 on 2021-07-03 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CastMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('castMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='castMember', to='tvcrib.castmember')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('year', models.IntegerField()),
                ('pg', models.IntegerField(default=None)),
                ('trailerLink', models.CharField(max_length=250)),
                ('movieCover', models.ImageField(blank=True, null=True, upload_to='')),
                ('cardCover', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ManyToManyField(related_name='category', to='tvcrib.Category')),
                ('character', models.ManyToManyField(related_name='character', to='tvcrib.Character')),
            ],
        ),
    ]
