# Generated by Django 4.1.2 on 2023-02-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0013_websettings_about_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]