# Generated by Django 3.1.3 on 2020-12-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_auto_20201201_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadcalender',
            name='img2',
            field=models.ImageField(default='', upload_to='static/images/'),
        ),
    ]
