# Generated by Django 2.2.6 on 2019-10-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_auto_20191024_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='main_pic',
            field=models.ImageField(default='default.jpg', upload_to='item_pics'),
        ),
    ]
