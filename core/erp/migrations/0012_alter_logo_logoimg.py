# Generated by Django 5.0.2 on 2024-03-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logoimg',
            field=models.ImageField(blank=True, null=True, upload_to='logo'),
        ),
    ]
