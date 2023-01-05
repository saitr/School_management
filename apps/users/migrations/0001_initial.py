# Generated by Django 4.1.4 on 2023-01-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_index=True, max_length=50, verbose_name='Username')),
                ('employee_id', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Employee ID')),
                ('password', models.CharField(db_index=True, max_length=255, verbose_name='Password')),
                ('email', models.EmailField(db_index=True, max_length=100, verbose_name='Email')),
                ('token', models.CharField(max_length=500, verbose_name='Token')),
                ('token_expires_at', models.DateTimeField(max_length=50, verbose_name='Token Expires at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]