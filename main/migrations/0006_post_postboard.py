# Generated by Django 2.0.7 on 2018-07-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180719_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postboard',
            field=models.CharField(default='/main/', max_length=32),
        ),
    ]
