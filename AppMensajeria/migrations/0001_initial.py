# Generated by Django 4.0.4 on 2022-06-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.CharField(max_length=200)),
                ('receptor', models.CharField(max_length=200)),
                ('cuerpo', models.CharField(max_length=200)),
                ('campo_leido', models.BooleanField()),
            ],
        ),
    ]
