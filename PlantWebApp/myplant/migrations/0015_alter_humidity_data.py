# Generated by Django 3.2.3 on 2021-08-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myplant', '0014_alter_humidity_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='data',
            field=models.CharField(default='plant_img', max_length=200),
        ),
    ]
