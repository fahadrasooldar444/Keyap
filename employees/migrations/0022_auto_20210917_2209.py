# Generated by Django 3.2.7 on 2021-09-17 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0021_auto_20210917_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='account_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.accountcategories'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='account_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.accounttypes'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employees'),
        ),
        migrations.AddField(
            model_name='accounttypes',
            name='account_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.accountcategories'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='holderid',
            field=models.IntegerField(db_column='holderID', default=1),
        ),
    ]