# Generated by Django 2.0.5 on 2018-07-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.PositiveIntegerField()),
                ('postcontent', models.CharField(max_length=256)),
            ],
        ),
    ]
