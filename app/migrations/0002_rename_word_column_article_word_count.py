# Generated by Django 5.1.4 on 2025-01-08 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='word_column',
            new_name='word_count',
        ),
    ]
