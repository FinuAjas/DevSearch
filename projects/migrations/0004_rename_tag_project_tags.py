# Generated by Django 4.0.4 on 2022-05-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_reviews_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
    ]
