# Generated by Django 3.1.3 on 2020-12-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0011_auto_20201203_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('year', models.CharField(blank=True, default='', max_length=100)),
                ('pdf_f', models.FileField(blank=True, default='', upload_to='static/pdfs/')),
            ],
        ),
    ]
