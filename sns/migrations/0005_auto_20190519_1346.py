# Generated by Django 2.1.7 on 2019-05-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0004_auto_20190519_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, default='defo', null=True, upload_to='documents/'),
        ),
    ]
