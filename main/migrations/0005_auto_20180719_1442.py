# Generated by Django 2.0.7 on 2018-07-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180719_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postimg',
            field=models.URLField(blank=True),
        ),
    ]
