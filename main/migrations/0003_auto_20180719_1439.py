# Generated by Django 2.0.7 on 2018-07-19 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_postimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postauthor',
            field=models.CharField(default='Anonymous', max_length=16),
        ),
        migrations.AddField(
            model_name='post',
            name='posttime',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='post',
            name='posttitle',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
