# Generated by Django 4.0.5 on 2022-06-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_services_introduction_cause5'),
    ]

    operations = [
        migrations.AddField(
            model_name='services_introduction',
            name='cause5',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]