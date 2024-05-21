# Generated by Django 5.0.1 on 2024-05-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='present_days',
            new_name='total_days_present',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_present',
            field=models.BooleanField(default=True),
        ),
    ]