# Generated by Django 3.1.4 on 2020-12-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]