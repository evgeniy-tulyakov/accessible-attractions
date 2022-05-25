# Generated by Django 4.0.4 on 2022-05-25 17:35

import functools

from django.db import migrations, models

import server.utilites



class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_photo'),
    ]


    operations = [

        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('content', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'О нас',
                'db_table': 'about_us_page',
            },
        ),

        migrations.AlterField(
            model_name='attraction',
            name='audio_description',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=functools.partial(server.utilites.build_upload_path, *('audio',), **{}),
                verbose_name='Аудио описание'
            ),
        ),

        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(
                upload_to=functools.partial(server.utilites.build_upload_path, *('photo',), **{}),
                verbose_name='Изображение'
            ),
        ),

    ]