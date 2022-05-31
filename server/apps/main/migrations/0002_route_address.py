# Generated by Django 4.0.4 on 2022-05-31 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='address',
            field=models.CharField(
                default='undefined',
                max_length=128,
                unique=True,
                verbose_name='Адрес'
            ),
        ),
    ]