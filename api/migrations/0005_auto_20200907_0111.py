# Generated by Django 3.0.5 on 2020-09-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200907_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldsdata',
            name='options_list',
            field=models.ManyToManyField(blank=True, to='api.OptionList'),
        ),
        migrations.AlterField(
            model_name='fieldsdata',
            name='options_url',
            field=models.ManyToManyField(blank=True, to='api.OptionsUrl'),
        ),
    ]
