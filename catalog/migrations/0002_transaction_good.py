# Generated by Django 3.0.6 on 2020-07-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='good',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
