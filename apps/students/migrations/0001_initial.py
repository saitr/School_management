# Generated by Django 4.1.4 on 2023-01-03 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_classes', '0001_initial'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_roll', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], max_length=20, verbose_name='title')),
                ('firstname', models.CharField(db_index=True, max_length=100, verbose_name='First Name')),
                ('lastname', models.CharField(db_index=True, max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=500, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50, verbose_name='Gender')),
                ('father', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Father Name')),
                ('mother', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Mother Name')),
                ('gaurdian', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Gaurdian Name')),
                ('adhaar', models.IntegerField(verbose_name='Aadhar')),
                ('domicile', models.IntegerField(verbose_name='Domicile Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='UpdatedAt')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_results', to='results.declareresult')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_classes.studentclass')),
            ],
            options={
                'db_table': 'Students',
            },
        ),
    ]
