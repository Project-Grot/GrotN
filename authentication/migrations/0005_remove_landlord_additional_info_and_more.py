# Generated by Django 4.2.11 on 2024-06-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_landlord_additional_info_landlord_basecity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landlord',
            name='additional_info',
        ),
        migrations.AddField(
            model_name='landlord',
            name='additionalInfo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
