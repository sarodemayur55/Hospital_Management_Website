# Generated by Django 3.1.6 on 2021-05-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_doctordata_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_appointment',
            name='doctorusername',
            field=models.CharField(default='', max_length=50),
        ),
    ]
