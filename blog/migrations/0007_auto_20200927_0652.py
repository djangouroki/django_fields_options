# Generated by Django 3.1 on 2020-09-27 06:52

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200927_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default='2020-02-01', verbose_name='published date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, db_index=True, default=blog.models.get_default_text, unique_for_date='pub_date', verbose_name='text'),
        ),
    ]