# Generated by Django 2.0.6 on 2018-11-03 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20181101_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id'], 'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
    ]
