# Generated by Django 2.2.4 on 2021-07-30 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
