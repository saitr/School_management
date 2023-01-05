# Generated by Django 4.1.4 on 2023-01-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclass',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentclass',
            name='class_name',
            field=models.CharField(help_text='Eg- Third, Fouth,Sixth etc', max_length=100),
        ),
    ]