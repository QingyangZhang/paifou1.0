# Generated by Django 3.0.6 on 2020-07-07 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_transaction_good'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='prefer',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='major',
        ),
        migrations.AddField(
            model_name='customer',
            name='prefer1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_prefer1', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='customer',
            name='prefer2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_prefer2', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='customer',
            name='prefer3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_prefer3', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='saler',
            name='major1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saler_major1', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='saler',
            name='major2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saler_major2', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='saler',
            name='major3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saler_major3', to='catalog.Genre'),
        ),
    ]
