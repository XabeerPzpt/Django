# Generated by Django 5.0.1 on 2024-05-10 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='email',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
    ]
