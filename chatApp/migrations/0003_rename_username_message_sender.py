# Generated by Django 5.0 on 2024-05-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0002_rename_sender_message_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='username',
            new_name='sender',
        ),
    ]