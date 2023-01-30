# Generated by Django 4.0.2 on 2023-01-30 08:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_comment_short_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 8, 47, 54, 689217, tzinfo=utc), verbose_name='Time created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 8, 47, 54, 688383, tzinfo=utc), verbose_name='Time Created'),
        ),
    ]
