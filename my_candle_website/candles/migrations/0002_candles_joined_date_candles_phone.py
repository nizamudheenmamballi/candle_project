# Generated by Django 4.1.7 on 2023-05-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candles',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='candles',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
