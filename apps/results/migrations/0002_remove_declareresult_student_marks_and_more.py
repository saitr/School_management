# Generated by Django 4.1.4 on 2023-01-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declareresult',
            name='student_marks',
        ),
        migrations.AddField(
            model_name='declareresult',
            name='student_marks',
            field=models.ManyToManyField(blank=True, to='results.studentmarks'),
        ),
    ]
