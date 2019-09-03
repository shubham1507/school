# Generated by Django 2.2.2 on 2019-09-03 04:41

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190903_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
