# Generated by Django 2.0.6 on 2018-11-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20181103_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='page_url',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='博文主页'),
        ),
    ]
