# Generated by Django 2.2.5 on 2019-09-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorshots', '0012_auto_20190910_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='clave',
            field=models.CharField(default='', max_length=50),
        ),
    ]
