# Generated by Django 5.0.1 on 2024-01-17 12:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0010_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_text', ckeditor.fields.RichTextField()),
                ('twitter', models.URLField(max_length=255, verbose_name='Twitter')),
                ('facebook', models.URLField(max_length=255, verbose_name='Facebook')),
                ('linkedin', models.URLField(max_length=255, verbose_name='LinkedIn')),
                ('privacy_police', models.URLField(max_length=255, verbose_name='Privacy Policy')),
                ('tou', models.URLField(max_length=255, verbose_name='Terms of Use')),
            ],
            options={
                'verbose_name_plural': 'Footer Items',
            },
        ),
    ]
