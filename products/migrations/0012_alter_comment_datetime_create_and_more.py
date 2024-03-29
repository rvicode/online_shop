# Generated by Django 4.0.2 on 2023-01-30 08:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_comment_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 8, 33, 12, 685400, tzinfo=utc), verbose_name='Time created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 8, 33, 12, 684564, tzinfo=utc), verbose_name='Time Created'),
        ),
    ]
