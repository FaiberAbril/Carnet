# Generated by Django 5.0.2 on 2024-03-05 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_alter_client_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Regional')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regional',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='cli',
        ),
        migrations.RemoveField(
            model_name='detsale',
            name='prod',
        ),
        migrations.RemoveField(
            model_name='detsale',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cate',
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('tipoDocumento', models.CharField(choices=[('Cédula de ciudadanía', 'CC'), ('Cédula de extranjería', 'CE'), ('NIT', 'NI'), ('Tarjeta de identidad', 'TI'), ('Registro civil de nacimiento', 'RC'), ('Pasaporte', 'PSP'), ('Documento de identificación extranjero', 'DIE'), ('Salvoconducto de permanencia', 'SP')], default='C.C', max_length=50, verbose_name='TipoDocumento')),
                ('numeroDocumento', models.CharField(blank=True, max_length=10, null=True, verbose_name='numeroDocumento')),
                ('tipoSangre', models.CharField(choices=[('O negativo', 'O-'), ('O positivo', 'O+'), ('A negativo', 'A-'), ('A positivo', 'A+'), ('B negativo', 'B-'), ('B positivo', 'B+'), ('AB negativo', 'AB-'), ('AB positivo', 'AB+')], default='0-', max_length=50, verbose_name='TipoDocumento')),
                ('cargo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.cargo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Centro')),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.regional')),
            ],
            options={
                'verbose_name': 'Centro',
                'verbose_name_plural': 'Centros',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='municipality',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='DetSale',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
