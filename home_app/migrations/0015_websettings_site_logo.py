# Generated by Django 4.1.2 on 2023-02-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0014_ourteam_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='websettings',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to='site_logo'),
        ),
    ]
