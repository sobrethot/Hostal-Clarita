# Generated by Django 3.2.4 on 2021-06-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedadew', '0009_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
    ]
