# Generated by Django 2.1 on 2018-10-12 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='pinTime',
            field=models.CharField(default=2, max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
            preserve_default=False,
        ),
    ]
