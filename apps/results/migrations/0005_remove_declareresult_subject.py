# Generated by Django 4.1.4 on 2023-01-04 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_alter_declareresult_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declareresult',
            name='subject',
        ),
    ]
