# Generated by Django 3.2.4 on 2021-06-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210623_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('PostId', models.AutoField(primary_key=True, serialize=False)),
                ('GmailId', models.EmailField(max_length=254)),
                ('File', models.ImageField(upload_to='')),
                ('Likes', models.IntegerField()),
            ],
        ),
    ]