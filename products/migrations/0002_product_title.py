# Generated by Django 4.0.2 on 2022-11-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
