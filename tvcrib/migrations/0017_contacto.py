# Generated by Django 3.2.4 on 2021-07-04 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrib', '0016_auto_20210704_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
