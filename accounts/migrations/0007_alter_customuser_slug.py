# Generated by Django 3.2.16 on 2022-12-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
