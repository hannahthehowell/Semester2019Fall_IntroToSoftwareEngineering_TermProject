# Generated by Django 2.2.6 on 2019-11-08 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_item_auction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_live_item',
        ),
    ]