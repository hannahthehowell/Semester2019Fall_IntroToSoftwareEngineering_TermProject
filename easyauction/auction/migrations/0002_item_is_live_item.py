# Generated by Django 2.2.6 on 2019-11-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_live_item',
            field=models.BooleanField(default=False),
        ),
    ]