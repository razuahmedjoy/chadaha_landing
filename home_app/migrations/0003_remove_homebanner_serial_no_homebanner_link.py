# Generated by Django 4.1.2 on 2023-01-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_donationimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homebanner',
            name='serial_no',
        ),
        migrations.AddField(
            model_name='homebanner',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
