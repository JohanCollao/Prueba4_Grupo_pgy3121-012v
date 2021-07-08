# Generated by Django 3.2.4 on 2021-07-07 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicio_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.servicio')),
            ],
        ),
    ]
