# Generated by Django 5.0.3 on 2024-03-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_pensionsupport_birth_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='childcaresupport',
            name='income_proof',
            field=models.FileField(blank=True, null=True, upload_to='income_proof/'),
        ),
    ]
