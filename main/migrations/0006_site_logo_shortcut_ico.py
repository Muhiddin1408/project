# Generated by Django 4.0.5 on 2022-06-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_footer_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_logo',
            name='shortcut_ico',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]