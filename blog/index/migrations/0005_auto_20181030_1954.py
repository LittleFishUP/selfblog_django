# Generated by Django 2.0.6 on 2018-10-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20181030_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img_url',
            field=models.ImageField(null=True, upload_to='static/blog_main/blogimg/', verbose_name='博客图示'),
        ),
    ]