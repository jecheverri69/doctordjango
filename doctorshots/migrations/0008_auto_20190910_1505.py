# Generated by Django 2.2.5 on 2019-09-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorshots', '0007_auto_20190910_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
