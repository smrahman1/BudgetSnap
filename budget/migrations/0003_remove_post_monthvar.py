# Generated by Django 3.2.5 on 2021-08-08 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_post_monthvar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='monthVar',
        ),
    ]
