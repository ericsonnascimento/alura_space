# Generated by Django 4.2.7 on 2023-11-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto/%Y/%m/%d'),
        ),
    ]
