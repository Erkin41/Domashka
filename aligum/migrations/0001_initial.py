# Generated by Django 4.0.4 on 2022-05-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.FileField(upload_to='')),
                ('image_2', models.FileField(upload_to='')),
                ('image_3', models.FileField(upload_to='')),
                ('image_5', models.FileField(upload_to='')),
                ('image_6', models.FileField(upload_to='')),
                ('image_7', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='image/%Y/%m/%d')),
                ('Shapka', models.CharField(blank=True, db_index=True, max_length=255)),
                ('title', models.CharField(blank=True, db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('description_2', models.TextField(blank=True)),
                ('description_3', models.TextField(blank=True)),
            ],
        ),
    ]
