# Generated by Django 5.1.1 on 2024-12-07 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='helpful_votes',
        ),
        migrations.AddField(
            model_name='reviews',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.bookings'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.TextField(max_length=1000),
        ),
    ]
