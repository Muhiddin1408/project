# Generated by Django 4.0.5 on 2022-06-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=455)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=155)),
                ('number2', models.CharField(blank=True, max_length=155)),
                ('email', models.CharField(blank=True, max_length=155)),
            ],
        ),
    ]
