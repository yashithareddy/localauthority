# Generated by Django 5.0.3 on 2024-03-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_healthsubsidy_income_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='pensionsupport',
            name='birth_certificate',
            field=models.FileField(blank=True, null=True, upload_to='birth_certificates/'),
        ),
    ]
