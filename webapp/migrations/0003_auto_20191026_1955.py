# Generated by Django 2.0.8 on 2019-10-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191026_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='r_logo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
