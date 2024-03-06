# Generated by Django 5.0.2 on 2024-03-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_formacion_rename_persona_aprendiz_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formacion',
            options={'ordering': ['id'], 'verbose_name': 'Formacion', 'verbose_name_plural': 'Formaciones'},
        ),
        migrations.AlterField(
            model_name='aprendiz',
            name='cargo',
            field=models.CharField(default='Aprendiz', max_length=30),
        ),
        migrations.AlterField(
            model_name='formacion',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Formacion'),
        ),
    ]