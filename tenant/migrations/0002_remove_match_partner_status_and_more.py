# Generated by Django 4.2.11 on 2024-06-04 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='partner_status',
        ),
        migrations.RemoveField(
            model_name='match',
            name='tenant_status',
        ),
    ]
