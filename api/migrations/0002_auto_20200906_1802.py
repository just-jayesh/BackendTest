# Generated by Django 3.0.5 on 2020-09-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldsdata',
            name='options_url',
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='fields',
            field=models.ManyToManyField(to='api.FieldsData'),
        ),
        migrations.AlterField(
            model_name='fieldsdata',
            name='options_list',
            field=models.ManyToManyField(to='api.OptionList'),
        ),
    ]