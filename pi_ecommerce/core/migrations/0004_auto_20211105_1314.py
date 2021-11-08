# Generated by Django 3.2.9 on 2021-11-05 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='code_prod',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='item',
            name='name_long',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='name_prod',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='characteristic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.caracteristica'),
        ),
    ]
