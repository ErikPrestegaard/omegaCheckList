# Generated by Django 3.1.6 on 2021-05-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daBookStore', '0002_auto_20210528_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklists',
            name='values',
            field=models.CharField(default='test', max_length=32),
        ),
    ]
