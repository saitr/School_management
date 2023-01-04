# Generated by Django 4.1.4 on 2023-01-03 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_remove_subject_results'),
        ('results', '0002_declareresult_select_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='declareresult',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
            preserve_default=False,
        ),
    ]
