# Generated by Django 2.0.6 on 2018-11-01 03:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20181030_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img_url',
            field=models.ImageField(null=True, upload_to='static/blog_main/blogimg/', verbose_name='主页博客图片'),
        ),
    ]
