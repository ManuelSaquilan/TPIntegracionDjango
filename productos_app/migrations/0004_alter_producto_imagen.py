# Generated by Django 4.2.3 on 2023-07-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/images', verbose_name='Imagen'),
        ),
    ]
