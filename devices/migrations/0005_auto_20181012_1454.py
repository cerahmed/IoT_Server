# Generated by Django 2.1 on 2018-10-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_auto_20181012_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='lastTime',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
