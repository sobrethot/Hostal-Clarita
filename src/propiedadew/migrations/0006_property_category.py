# Generated by Django 3.2.4 on 2021-06-09 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedadew', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='propiedadew.category'),
        ),
    ]
