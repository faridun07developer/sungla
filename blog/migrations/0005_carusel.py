# Generated by Django 4.2.7 on 2024-02-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_haqida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]