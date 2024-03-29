# Generated by Django 2.2.5 on 2019-09-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorshots', '0015_usuarios_nombres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=45)),
                ('precioVenta', models.FloatField()),
                ('precioCompra', models.FloatField()),
                ('habilitado', models.BooleanField(default=True)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
