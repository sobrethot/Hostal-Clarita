# Generated by Django 3.2.4 on 2021-06-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedadew', '0003_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='propiedadew/'),
        ),
    ]
