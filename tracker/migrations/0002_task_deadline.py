# Generated by Django 4.2.2 on 2023-06-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
