# Generated by Django 3.2.9 on 2021-11-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_prod', models.CharField(max_length=23)),
                ('name_prod', models.CharField(max_length=48)),
                ('name_long', models.CharField(max_length=253)),
                ('date_create', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]