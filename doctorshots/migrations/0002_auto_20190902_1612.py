# Generated by Django 2.2.3 on 2019-09-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorshots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('usuario', models.CharField(max_length=150, unique=True)),
                ('contraseña', models.CharField(max_length=150)),
                ('Rol', models.CharField(choices=[('1', 'empleado'), ('2', 'administrador')], default='1', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
