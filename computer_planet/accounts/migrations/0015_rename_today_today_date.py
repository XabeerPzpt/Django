# Generated by Django 5.0.1 on 2024-05-21 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_today'),
    ]

    operations = [
        migrations.RenameField(
            model_name='today',
            old_name='today',
            new_name='date',
        ),
    ]