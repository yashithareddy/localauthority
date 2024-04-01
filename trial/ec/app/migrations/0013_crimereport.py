# Generated by Django 5.0.3 on 2024-03-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_lowincomesupportapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('reporter_name', models.CharField(max_length=100)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
