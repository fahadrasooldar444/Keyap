# Generated by Django 3.2.7 on 2021-09-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
