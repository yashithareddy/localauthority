# Generated by Django 5.0.3 on 2024-03-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_healthsubsidy_applicant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthsubsidy',
            name='medical_history',
            field=models.TextField(default='No medical history provided'),
        ),
    ]
