# Generated by Django 3.2.3 on 2021-07-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myplant', '0009_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
    ]
