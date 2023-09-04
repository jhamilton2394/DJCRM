# Generated by Django 4.2.2 on 2023-08-31 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_passdown_time_alter_passdown_shift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='passdown',
        ),
        migrations.AddField(
            model_name='passdown',
            name='entry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='leads.entry'),
            preserve_default=False,
        ),
    ]
