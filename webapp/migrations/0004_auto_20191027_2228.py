# Generated by Django 2.2.6 on 2019-10-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191026_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Acknowledged', 'Acknowledged'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Dispatched', 'Dispatched')], default='Placed', max_length=50),
        ),
    ]