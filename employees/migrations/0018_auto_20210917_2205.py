# Generated by Django 3.2.7 on 2021-09-17 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_auto_20210917_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cashnds',
            options={},
        ),
        migrations.DeleteModel(
            name='Cnds',
        ),
    ]
