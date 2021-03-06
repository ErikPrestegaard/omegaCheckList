# Generated by Django 3.1.6 on 2021-05-28 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daBookStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='checklistValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('isChecked', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('belongsTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daBookStore.checklists')),
            ],
        ),
        migrations.DeleteModel(
            name='books',
        ),
    ]
