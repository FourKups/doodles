# Generated by Django 3.2.4 on 2021-06-23 07:25

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_delete_lost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='File',
            field=models.ImageField(upload_to=login.models.update_filename),
        ),
        migrations.AlterField(
            model_name='post',
            name='Likes',
            field=models.IntegerField(default=0),
        ),
    ]
