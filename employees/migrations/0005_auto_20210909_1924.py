# Generated by Django 3.2.7 on 2021-09-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20210909_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='contract_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employees',
            name='cpr_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employees',
            name='license_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employees',
            name='passport_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employees',
            name='visa_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
