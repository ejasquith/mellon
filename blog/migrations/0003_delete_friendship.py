# Generated by Django 3.2.16 on 2022-12-28 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_friendship'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]
